"""Project6Fab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Apps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.firstPage),
    url(r'^home/', views.registerview),
    url(r'^detailpage/', views.student_details),
    url(r'^comments/', views.comment_history),
    url(r'^allcomments/', views.allCommentsView),
    url(r'^loginview/',views.loginView),
    url(r'^logout/',views.session_log_out),
    url(r'^save_note/',views.note_save_view),
]
