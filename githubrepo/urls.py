from django.conf.urls import url

from githubrepo import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^lijstbestanden/$', views.lijstbestanden, name='lijstbestanden'),
  url(r'^lijstrepos/$', views.lijstrepos, name='lijstrepos'),
]