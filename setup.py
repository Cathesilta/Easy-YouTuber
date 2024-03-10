import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    packages = [
        "google-api-python-client",
        "oauth2client",
        "http",
        "httplib2"
    ]

    for package in packages:
        try:
            install(package)
            print(f"Successfully installed {package}")
        except Exception as e:
            print(f"Error installing {package}: {e}")