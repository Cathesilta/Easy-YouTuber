#!/usr/bin/env python3

import http.client
import httplib2
import os
import random
import sys
import time
import pdb
import yaml

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
  http.client.IncompleteRead, http.client.ImproperConnectionState,
  http.client.CannotSendRequest, http.client.CannotSendHeader,
  http.client.ResponseNotReady, http.client.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


with open('./config.yml','r') as f:
  config_yml = yaml.safe_load(f)
  


CLIENT_SECRETS_FILE = config_yml['Dependent_File']['client_secrets_file']
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = "client secret's not found, check it"
VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

proxy_routing_address = config_yml['Proxy']['address']
proxy_routing_port = config_yml['Proxy']['port']

os.environ["http_proxy"] = f"http://{proxy_routing_address}:{proxy_routing_port}"
os.environ["https_proxy"] = f"https://{proxy_routing_address}:{proxy_routing_port}"

# Proxy configuration
PROXY_INFO = httplib2.ProxyInfo(
    proxy_type=httplib2.socks.PROXY_TYPE_HTTP, 
    proxy_host= proxy_routing_address, 
    proxy_port=int(proxy_routing_port)
)

if config_yml['Proxy']['use_proxy'] == 1:
  proxied_http = httplib2.Http(proxy_info=PROXY_INFO)
else:
  proxied_http = httplib2.Http()

def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_UPLOAD_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage(f"{sys.argv[0]}-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
      credentials = run_flow(flow, storage, args)

    # Update to use the proxy
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                http=credentials.authorize(proxied_http))

def initialize_upload(youtube, options):
  tags = None
  if options.keywords:
    tags = options.keywords.split(",")

  body = {
    "snippet": {
      "title": options.title,
      "description": options.description,
      "tags": tags,
      "categoryId": options.category
    },
    "status": {
      "privacyStatus": options.privacyStatus
    }
  }

  insert_request = youtube.videos().insert(
    part=",".join(body.keys()),
    body=body,
    media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
  )

  resumable_upload(insert_request)

def resumable_upload(insert_request):
  response = None
  error = None
  retry = 0
  while response is None:
    try:
      print("Uploading file...")
      status, response = insert_request.next_chunk()
      if 'id' in response:
        print(f"Video id '{response['id']}' was successfully uploaded.")
      else:
        sys.exit("The upload failed with an unexpected response: %s" % response)
    except HttpError as e:
      if e.resp.status in RETRIABLE_STATUS_CODES:
        error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
      else:
        raise
    except RETRIABLE_EXCEPTIONS as e:
      error = "A retriable error occurred: %s" % e

    if error is not None:
      print(error)
      retry += 1

# The rest of your main code including argparser setup remains the same

if __name__ == '__main__':
    argparser.add_argument("--file", required=True, help="Video file to upload")
    argparser.add_argument("--title", help="Video title", default="Test Title")
    argparser.add_argument("--description", help="Video description",
      default="Test Description")
    argparser.add_argument("--category", default="20",
      help="Numeric video category. " +
        "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
    argparser.add_argument("--keywords", help="Video keywords, comma separated",
      default="")
    argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
      default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
    
    args = argparser.parse_args()

    if not os.path.exists(args.file):
      exit("Please specify a valid file using the --file= parameter.")
      
    youtube = get_authenticated_service(args)
    try:
      initialize_upload(youtube, args)
    except HttpError as e:
      print("An HTTP error {} occurred:\n{}".format(e.resp.status, e.content))