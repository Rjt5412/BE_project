from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^keysearch/$', views.search, name='search'),
    url(r'^get_params/$', views.get_params, name='get_params'),
    url(r'^about_us$', views.about_us, name='about_us'),
    #url(r'^main_cat', views.get_main_category, name='main_cat_url'),
    #url(r'^keysearch/(?P<m_id>\d+)/', views.get_sub_category, name='sub_cat_url')
]