
from django.urls import path
from django.contrib.auth import views as auth_views
from  . import views

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.delete, name='delete'),

]