from django.conf.urls import patterns
from django.conf.urls import url
from rango import views

urlpatterns=patterns('',
		url(r'^$',views.index,name='index'),
		url(r'^about/$',views.about,name='about'),
		url(r'^aboutphu/$',views.about_phu,name='aboutphu'))