from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^keysearch/$', views.search, name='search'),
    url(r'^get_params/$', views.get_params, name='get_params'),
    url(r'^about_us$', views.about_us, name='about_us'),
]