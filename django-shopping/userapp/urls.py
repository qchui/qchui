from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register$', views.RegisterView.as_view()),
    url(r'checkUname/$', views.CheckUanemView.as_view()),
    url(r'center$', views.CenterUanemView.as_view()),
    url(r'logout/$', views.Logoutviews.as_view()),
    url(r'login/$', views.Loginviews.as_view()),
    url(r'address/$', views.Addressviews.as_view()),
    url(r'loadarea/$', views.Loadviews.as_view()),

]
