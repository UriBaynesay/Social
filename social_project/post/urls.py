from django.urls import path
from .views import home, post_details, post_create

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_details, name='post-details'),
    path('post/new/', post_create, name='post-create')
]
