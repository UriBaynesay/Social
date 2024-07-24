from django.urls import path
from .views import home, post_details, post_create, post_update, post_delete, _add_like, _delete_like

urlpatterns = [
    path('', home, name='home'),
    path('like/new/', _add_like, name='create-like'),
    path('like/delete/<int:post_id>/', _delete_like, name='delete-like'),
    path('post/<int:pk>/', post_details, name='post-details'),
    path('post/update/<int:pk>/', post_update, name='post-update'),
    path('post/new/', post_create, name='post-create'),
    path('post/delete/<int:pk>', post_delete, name='post-delete')
]
