from django.urls import path
from .views import home,logout,login,like_blog,category


urlpatterns = [
    path('',home,name='blog'),
    path('category/<slug:slug>/',category,name='category'),
    path('like/<str:pk>/',like_blog,name='like'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
]
