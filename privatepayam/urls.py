from django.conf.urls import url , include
from django.contrib.auth.views import LoginView,LogoutView


from .views import PVList , ListOfPV 


urlpatterns = [

    url(r'^to/(?P<slug>\w+)/$',PVList.as_view() ,name='to' ),
    url(r'^send/$',ListOfPV.as_view() ,name='send' ),
    # url(r'^remove/(?P<slug>\w+)/$',RemovePVList.as_view() ,name='remove' ),
]
