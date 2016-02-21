"""sg_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

from django.contrib.sitemaps.views import sitemap

import pfolio
from pfolio.models import blogPostSitemap,portfolioPostSitemap

sitemaps = {blogPostSitemap,portfolioPostSitemap}

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ###
    # URl starting at /
    ###
    url(r'^', include('pfolio.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


###### IF URL IS NOT MATCHED FALL BACK TO ANGULAR CONTROL BY LOADING INDEX.HTML ######
urlpatterns +=[
    url(r'^.*$', pfolio.views.HomePageView.as_view())
]