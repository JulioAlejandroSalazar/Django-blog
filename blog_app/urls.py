from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post', views.create_post, name='create_post'),
    path('view-post-<id>', views.get_post, name='get_post'),
    path('edit-post-<id>', views.edit_post, name='edit_post'),
    path('delete-post-<id>', views.delete_post, name='delete_post'),
]