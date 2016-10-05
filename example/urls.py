"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
from django.conf.urls import include

from rest_framework import routers

from .world import views

router = routers.DefaultRouter()

router.register(r'city', views.CityViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'countrylanguage', views.CountrylanguageViewSet)

urlpatterns = [url(r'^', include(router.urls)),url(r'^api-docs', views.schema_view),]
