from django.urls import path
from .views import index,post
urlpatterns = [
    path('',index,name='blog_page'),
    path('<slug:slug>/',post,name='post')

]