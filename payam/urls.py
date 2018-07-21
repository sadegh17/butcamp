from django.conf.urls import url , include
from django.contrib.auth.views import LoginView,LogoutView

from .views import DeleteMessage , message_list , FollowingsView ,FollowersView



urlpatterns = [
    url(r'^$',message_list ,name='list' ),
    url(r'^followers/(?P<slug>\w+)/$',FollowersView.as_view() ,name='followers' ),
    url(r'^followings/(?P<slug>\w+)/$',FollowingsView.as_view() ,name='followings' ),
    url(r'^remove/(?P<pk>\d+)/$',DeleteMessage.as_view() ,name='remove' ),

]
