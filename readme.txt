Django1.10+创建项目，创建app实战（两种方法）

方法一
安装django后会有django-admin命令，通过django-admin startproject mysite
# cd E:\django\project
1项目创建
使用 django-admin.py 来创建一个项目:
-> django-admin  startproject  hellodjango
-> cd  hellodjango
创建完成后我们可以查看下项目的目录结构：
> cd hellodjango
 
> tree
|-- hellodjango
 
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
目录说明：
hellodjango 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
hellodjango/__init__.py: 一个空文件，告诉Python 该目录是一个 Python 包。
hellodjango/settings.py: 该 Django 项目的设置/配置。
hellodjango/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
hellodjango/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
 
启动服务器
-> python manage.py runserver 0.0.0.0:8000
0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。
 
启动服务：
-> 打开浏览器键入：127.0.0.1:8000
2创建app
> python manage.py startapp  Test
3. 在Test的views.py文件里写
from django.shortcuts import render
from django.http import HttpResponse
def  index(request):
     return HttpResponse("Hello,world.")
4在Test目录中，先创建一个urls.py文件
from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index, name='index'),
]
 
5．在根url模块中加入Test.urls模块,在HelloDjango目录下的urls.py中写入以下代码
from django.conf.urls import include, url,include
from django.contrib import admin
from . import views
urlpatterns = [
  url(r'^Test/', include('Test.urls')),
  url(r'^admin/', admin.site.urls),
]
6运行 python manager.py runserver
http://localhost/Test
 
7.视图和 URL 配置
E:\django\project\hellodjango\hellodjango\view.py 文件代码：
在先前创建的 hellodjango 目录下的 hellodjango 目录新建一个 view.py 文件，并输入代码
from django.http import HttpResponse
def hello(request):
return HttpResponse("Hello world ! ")
接着，绑定 URL 与视图函数。打开E:\django\project\hellodjango\hellodjango\ urls.py 文件，删除原来代码，将以下代码复制粘贴到 urls.py 文件中：
from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^$', view.hello),
]
完成后，启动 Django 开发服务器，并在浏览器访问打开浏览器并访问：http://localhost:8000
|-- hellodjango
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- urls.py              # url 配置
|   |-- urls.pyc
|   |-- view.py              # 添加的视图文件
|   |-- view.pyc             # 编译后的视图文件
|   |-- wsgi.py
|   `-- wsgi.pyc
`-- manage.py
 
我们也可以修改以下规则：
hellodjagon/hellodjango/urls.py 文件代码：
from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^hello$', view.hello),
]
通过浏览器打开 http://127.0.0.1:8000/hello，输出结果如下：
 
注意：项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启
 
 
url() 函数
Django url() 可以接收四个参数，分别是两个必选参数：regex、view 和两个可选参数：kwargs、name，接下来详细介绍这四个参数。
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。



方法二
安装django后会有django-admin命令，通过django-admin startproject mysite
1项目创建mydjango
>cd E:\django\project
->django-admin  startproject  mydjango
2.创建app
>python manager.py startapp blog
3. 设置E:\django\project\mydjango\mydjango\setting.py
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-hans'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
添加blog
4. 设置E:\django\project\mydjango\mydjango\urls.py
from django.conf.urls import url
from django.contrib import admin
from blog.views  import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',index),
]
5.E:\django\project\mydjango\blog\views.py
#coding:utf-8
from django.shortcuts import render
from  django.http  import  HttpResponse
# Create your views here.
def  index(request):
     return HttpResponse(u'
hello world欢迎使用django1.10
')
6. >python manage.py runserver
浏览器输入http://127.0.0.1:8000/index/