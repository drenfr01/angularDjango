from django.conf.urls import patterns, include, url
from rest_framework import routers
from interests import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^interests/', include('interests.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
