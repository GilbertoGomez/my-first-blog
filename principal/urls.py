from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
	url(r'^$',views.index ),
	url(r'^blog',views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new,name='post_new'),
]