"""Haedal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# main 어플리케이션의 view에서 index 페이지를 불러오자
from main.views import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 웹사이트의 첫 화면은 index 페이지이다.
    # https://yebin0514.run.goorm.io
    path('', index),
]
