from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.eric, name="eric"),
    url(r'^(?P<question_id>[0-9]+)/result$', views.result, name="result"),

]