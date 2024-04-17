from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.categories, name='categories'),
    path('post/', views.posts, name='post'),
]