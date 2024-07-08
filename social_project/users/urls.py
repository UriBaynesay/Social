from django.urls import path
from .views import register, profile, delete
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('delete/<int:pk>', delete, name='user-delete'),
]
