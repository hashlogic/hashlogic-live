from django.contrib import admin
from django.urls import path, include
# from .views import  PostDetailView
from . import views


urlpatterns=[
	path('blog/', views.blog, name='blog'),
    # path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/<int:pk>/', views.single_blog, name='single_blog'),
    
]