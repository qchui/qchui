from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AddCartView.as_view()),
    url(r'^queryAll$', views.QueryALlView.as_view()),

]
