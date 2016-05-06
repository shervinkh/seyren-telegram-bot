from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<alert_url>.*)/$', views.seyren_notification, name='seyren_notification'),
]