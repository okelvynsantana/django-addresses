from django.urls import path
from django.contrib import admin
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addresses/', views.address_list, name='address_list'),
    path('addresses/create/', views.address_create, name='address_create'),
    path(
        'addresses/<int:id>/update/',
        views.address_update,
        name='address_update'
    )
]
