from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.seyren_notification, name='seyren_notification'),
]