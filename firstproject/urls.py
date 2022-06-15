"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from audioop import add
from django.contrib import admin
from django.urls import path,re_path,include
from myapp.views import RegisterForm,index,test
from templates.my_tags import mul,my_input
import firstproject.testdb as testdb
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('test/', test),
    re_path(r'db/add$', testdb.add),
    path('db/getall/', testdb.getAll),
    re_path(r'db/update$', testdb.update),
    re_path(r'db/delete$', testdb.delete),
]
