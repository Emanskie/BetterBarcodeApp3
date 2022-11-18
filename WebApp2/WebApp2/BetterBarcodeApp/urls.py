from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.loginpage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('input/', views.studentinput, name="input"),
    path('todo/', views.alltodos, name = 'alltodo'),
    path('delete_item/<int:pk>', views.deleteItem, name = 'deleteItem'),
    path('update_item<int:pk>', views.updateItem, name = 'updateItem'),
    path('scanner/', views.scanner, name = 'scanner'),
]