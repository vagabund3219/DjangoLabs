
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstap import views
urlpatterns = [
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    re_path(r'^products/$', views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('', views.index,name='home'),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    path('admin/', admin.site.urls),
]
