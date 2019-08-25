from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexVie.as_view()),
    url(r'^categroy/(\d+)$', views.IndexVie.as_view()),
    url(r'^categroy/(\d+)/page/(\d+)$', views.IndexVie.as_view()),
    url(r'^goodsdetails/(\d+)$', views.DetailViwe.as_view()),


]
