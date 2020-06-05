from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('addresses/', views.address_list, name='address_list'),
    path('addresses/create/', views.address_create, name='address_create'),
    path(
        'addresses/<int:id>/update/',
        views.address_update,
        name='address_update'
    ),
    path('address/<int:id>/destroy', views.address_destroy, name='address_destroy')
]
