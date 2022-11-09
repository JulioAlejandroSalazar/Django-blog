from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('', views.my_profile, name='my_profile'),
    path('<username>', views.unaffiliated_profile, name='unaffiliated_profile'),
    path('all/', views.profile_all, name='profile_all'),
    path('change-password/', views.change_password, name='change_password'),
]