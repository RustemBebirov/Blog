from django.urls import path
from .views import home,logout,login,like_blog,category,blog_details,register,about,contact,create_blog



urlpatterns = [
    path('',home,name='blog'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('create/',create_blog,name='create_blog'),
    path('details/<str:pk>/',blog_details,name='details'),
    path('category/<slug:slug>/',category,name='category'),
    path('like/<str:pk>/',like_blog,name='like'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]
