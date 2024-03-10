# Easy-YouTuber
I make this repository to automate YouTube Repetitive operations, so far including uploading.



### 使用方法-中文


##### 需要的东西(准备工作)
###### 1. 系统安装Python(略，自己网上查，到处都是)
###### 2. 获得YouTube上传API凭据(写在下面)
###### 3. 通过Google `品牌审核(Brand Verification)`, 这一步最难，通常需要一个月。如果没通过，其他都百搭(如果没通过，用脚本上传的视频将无法公开public)。


##### 如何用脚本上传

###### `python upload_video.py --file file_name --title title_name --description video description --category 20 --keywords tags`
###### 其中，category没太多意义，如果您非常在意，可以查阅[YouTube视频类型列表](https://developers.google.com/youtube/v3/docs/videoCategories/list)


##### 上传时如何使用代理

###### 默认已经配置好了。如需更改，在`config.yml`中 的`Proxy`下，将`use_proxy`填为1；将`address`填成代理的地址(如果您用的是Clash，通常默认为127.0.0.1)；将`port`填为代理的端口(如果您用的是Clash，通常默认为7890).

##### 如何开启YouTube上传API

###### 1. 登录[Gooogle 开发者控制台(Developer Console)](https://console.developers.google.com/).
###### 1.5 如果你登入后是空白一片，点左上角的`创建项目(Create Project)`，此时你将被要求填写`项目名(Project Name)`, `组织(Organization)`, '地理位置(Location)', 请随意填写.
###### 2. 在新项目仪表板(Dashboard)上，单击浏览并`启用API(Explore & Enable APIs)`.
###### 3. 在库列表(Library)中，找到 YouTube API 下的 `YouTube Data API v3`。点击开启(Enable)后，您将进入一个概述(Overview)页面。在右上角，点击`创建凭据(Create Credentials)`.
###### 4. 在凭据窗口里，您将被问到`您要用哪一个API(Which API are you using?)`, 请选择`YouTube Data API v3`；以及`您将何处调用API(Where will you be calling API from?)`，请选择`Web server (e.g. node js. Tomcat)`；以及 `您将获取什么数据(What data will you be accessing?)`,选择`公共数据(Public data)`.
###### 5. 点击`(我需要什么凭证)What credentials do I need?`，点击`完成(Done)`.
###### 6. 好了，您将下载到一个凭据(.json文件)；以及以后但凡您还需要凭据，都可以去`凭据(Credentials)`窗口里去找到一个下载按钮。
