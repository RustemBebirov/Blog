from django.urls import path
from .views import home,logout,login,like_blog,category,blog_details,register


urlpatterns = [
    path('',home,name='blog'),
    path('details/<str:pk>/',blog_details,name='details'),
    path('category/<slug:slug>/',category,name='category'),
    path('like/<str:pk>/',like_blog,name='like'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]
