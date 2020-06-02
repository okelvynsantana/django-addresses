from django.urls import path
from django.contrib import admin
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')
]
