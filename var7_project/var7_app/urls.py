from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),

    path('', views.homePage, name = 'home'),
    path('user/', views.userPage, name = 'user'),

    path('contact/', views.contactPage, name = 'contact'),
    path('about/', views.aboutPage, name = 'about'),

    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]