"""butcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.contrib.auth.views import LoginView,LogoutView
from user.views import go_to_login  ,ProfUpdate , signup , Follow


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', go_to_login,name="home"),
    url(r'^signup/$', signup , name='signup'),
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login' ),
    url(r'^logout/$',LogoutView.as_view() ,name='logout' ),
    url(r'^update/(?P<slug>\w+)/$',ProfUpdate.as_view() ,name='update' ),
    url(r'^follow/$',Follow.as_view() ,name='follow' ),
    url(r'^payam/', include(('payam.urls', 'payam'), namespace='payam')),
    url(r'^pv/', include(('privatepayam.urls', 'privatepayam'), namespace='pv')),

]
