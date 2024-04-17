from django.urls import path
from . import views

urlpatterns = [
    path('category-list/',views.category_list),
    path('category-detail/<int:id>/',views.category_detail),
    path('post-list/',views.post_list),
    path('post-detail/<int:id>/',views.post_detail),
]
