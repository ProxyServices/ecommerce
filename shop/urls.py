from django.conf.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^shop/', views.product_list, name='product_list'),
    re_path(r'^contact/', views.contact, name='contact'),
    re_path(r'^media/', views.media_list, name='media_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)