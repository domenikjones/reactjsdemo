"""reactdemo URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns, urlpatterns
from django.contrib import admin
from rest_framework import routers
from apiv1.viewsets import AppartementViewSet, AppartementList, AppartementTypeViewSet


router = routers.DefaultRouter()
router.register(r'appartements', AppartementViewSet)
router.register(r'types', AppartementTypeViewSet)

urlpatterns += i18n_patterns('',
    # rest API
    url(r'^apiv1/appartementslist/', AppartementList.as_view()),
    url(r'^apiv1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^admin/', include(admin.site.urls)),

    # default
    url(r'^', 'demo.views.index'),
)

# debug media files
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)