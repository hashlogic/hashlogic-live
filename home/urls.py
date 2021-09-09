from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns=[
	path('', views.index, name='index'),
	path('contacts/', views.contacts, name='contacts'),
	path('service/', views.service, name='service'),
	path('about/', views.about, name='about'),
	path('profile/', views.profile, name='profile'),
]