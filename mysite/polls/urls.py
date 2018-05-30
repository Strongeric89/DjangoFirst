from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import ChartData

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/result$', views.detail, name="detail"),
    url(r'^api/data/$', views.get_data, name="api-data"),
    url(r'^api/chart/data/$', ChartData.as_view(), name="api-data-chart"),


]