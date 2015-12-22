"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import settings
from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import*
from django.contrib.auth.views import login, logout
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
    url(r'^register/$', register),
    url(r'^login/$', login, {'template_name': "login.html"}),
    url(r'^logout/$', ensure_logout),
    #url(r'^logout/$', logout, {'template_name': "logout.html"}),
    url(r'^index/$', index),
    url(r'^addlog/$', addlog),
    url(r'^profile/$', myprofile),
    url(r'^passwd_change/$',passwd_change),
    url(r'^mylog/(.+)/$', mylog),
    url(r'^img/$', img),
    url(r'^addstrgy/$', addstrgy),
    url(r'^showstrgy/(.+)/$', showstrgy),
    url(r'^myhope/$', myhope),
    url(r'^design/$', design),
    url(r'^result/(.+)/(.+)/$', result),
    url(r'^advice/$', advice),
    url(r'^my_advice_user/(.+)/$', my_advice_user),
    url(r'^deal_msg/(.+)/(.+)/$', deal_msg),
    url(r'^is_add_logimg/(.+)/$', is_add_logimg),
    url(r'^logimg/(.+)/$', logimg),
    url(r'^friend_logimgs/(.+)/$', friend_logimgs),
    url(r'^group/$', group),
    url(r'^myfriend/$', myfriend),
    url(r'^deal_act/$', deal_act),
    url(r'^site/$', site),
    url(r'^mysite/(.+)/$', mysite),
    url(r'^ensure/$',ensure),
    url(r'^rewrite_password/$',rewrite_password),
    url(r'^find_password/$',find_password),
    url(r'^visitor/$',visitor),
]
