from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
]