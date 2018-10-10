"""tripmaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import index,login_user,signup_user,logout_user, home
from trips.views import trip_manager,trip_detail,add_trip,nltk

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^login/$', login_user, name="login"),
    url(r'^signup/$', signup_user, name="signup"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'^home/$', home, name="home"),
    url(r'^trips/$', trip_manager, name="trips"),
    url(r'^trip-detail/(?P<pk>\d+)/$', trip_detail, name="trip-detail"),
    url(r'^add-trip/$', add_trip, name="add-trip"),
    url(r'^nltk/$', nltk, name="nltk"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)