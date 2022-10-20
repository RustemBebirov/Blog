from django.urls import path
from .views import home,logout,login,like_blog


urlpatterns = [
    path('',home,name='blog'),
    path('like/<str:pk>/',like_blog,name='like'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
]
