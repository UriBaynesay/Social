from django.urls import path
from .views import home, post_details, post_create, post_update

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_details, name='post-details'),
    path('post/update/<int:pk>/', post_update, name='post-update'),
    path('post/new/', post_create, name='post-create')
]
