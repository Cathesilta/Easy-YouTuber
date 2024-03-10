# Easy-YouTuber
I make this repository to automate YouTube Repetitive operations, so far including uploading.

## Usage
###### [中文使用方法](#使用方法-中文)

#### Prerequisites
##### 1。 Python.
##### 2.  [YouTube API](#get-youtube-upload-api-and-the-credential)
##### 3.  Pass "Google Brand Verification". This is the hardest step, normally taking one month. If you don't pass this verification, any video you upload with any script will remain private.

#### Installation

##### 1. `git clone https://github.com/Cathesilta/Easy-YouTuber.git`
##### 2. `cd Easy-YouTuber`
##### 3. `python setup.py`

#### Use the script to upload a YouTube video

##### 1.In `config.yml` file, fill out the [credential](#get-youtube-upload-api-and-the-credential) (a .json file) path.
##### 2. `python upload_video.py --file file_name --title title_name --description video description --category 20 --keywords tags`

#### Upload YouTube video through a proxy

##### The default configuration has already been set up. If you need to make changes, in the config.yml file under Proxy, set use_proxy to 0 as disabling the proxy; change address to the address of the proxy (if you are using Clash, it is usually set to 127.0.0.1 by default); set port to the port of the proxy (if you are using Clash, it is usually set to 7890 by default).


#### Get YouTube upload API and the credential

##### 1. Login [Gooogle (Developer Console)](https://console.developers.google.com/).
##### 1.5 Once you log in, you’ll automatically be taken to an empty dashboard if you haven't created any projects. On the upper right-hand corner, click Create Project.
##### 2. You’ll be taken to a screen where you can add a project name, select your organization, and select a location (URL).
##### 3. On the new project dashboard, click `Explore & Enable APIs`.
##### 4. In the library, find to `YouTube Data API v3` under `YouTube APIs`. Then click `Enable`.
##### 5. After clicking Enable, you’ll be taken to an overview page. On the top right corner, click `Create Credentials`.
##### 6. On the Credentials window, you'll be asking "Which API are you using?" Select `YouTube Data API v3`; "Where will you be calling API from?" Select `Web server (e.g. node js. Tomcat)`; "What data will you be accessing?" Check the `Public data` box.
##### 7. Right below that, click on the blue button titled `What credentials do I need?` After that, your API key will automatically load. Click `Done`. Now you'll get a .json file, that is what we use as the credential when we upload with script.
















## 使用方法-中文


#### 需要的东西(准备工作)
##### 1. 安装Python.
##### 2. 获得[YouTube上传API](#如何开启YouTube上传API并获得凭据)凭据.
##### 3. 通过Google `品牌审核(Brand Verification)`, 这一步最难，通常需要一个月。如果没通过，其他都百搭(如果没通过，用脚本上传的视频将无法公开public).



#### 本程序安装方法

##### 1. `git clone https://github.com/Cathesilta/Easy-YouTuber.git`
##### 2. `cd Easy-YouTuber`
##### 3. `python setup.py`

#### 如何此程序上传视频

##### `python upload_video.py --file file_name --title title_name --description video description --category 20 --keywords tags`
##### 备注：category没太多意义，如果您非常在意，可以查阅[YouTube视频类型列表](https://developers.google.com/youtube/v3/docs/videoCategories/list)


#### 上传时如何使用代理

##### 默认已经配置好了。如需更改，在`config.yml`中 的`Proxy`下，将`use_proxy`填为1；将`address`填成代理的地址(如果您用的是Clash，通常默认为127.0.0.1)；将`port`填为代理的端口(如果您用的是Clash，通常默认为7890).

#### 如何开启YouTube上传API并获得凭据

##### 1. 登录[Gooogle 开发者控制台(Developer Console)](https://console.developers.google.com/).
##### 1.5 如果你登入后是空白一片，点左上角的`创建项目(Create Project)`，此时你将被要求填写`项目名(Project Name)`, `组织(Organization)`, '地理位置(Location)', 请随意填写.
##### 2. 在新项目仪表板(Dashboard)上，单击浏览并`启用API(Explore & Enable APIs)`.
##### 3. 在库列表(Library)中，找到 YouTube API 下的 `YouTube Data API v3`。点击开启(Enable)后，您将进入一个概述(Overview)页面。在右上角，点击`创建凭据(Create Credentials)`.
##### 4. 在凭据窗口里，您将被问到`您要用哪一个API(Which API are you using?)`, 请选择`YouTube Data API v3`；以及`您将何处调用API(Where will you be calling API from?)`，请选择`Web server (e.g. node js. Tomcat)`；以及 `您将获取什么数据(What data will you be accessing?)`,选择`公共数据(Public data)`.
##### 5. 点击`(我需要什么凭证)What credentials do I need?`，点击`完成(Done)`.
##### 6. 好了，您将下载到一个凭据(.json文件)；以及以后但凡您还需要凭据，都可以去`凭据(Credentials)`窗口里去找到一个下载按钮.
