from django.urls import path
from . import views

urlpatterns = [
    path('posts/' , views.PostList.as_view() , name='posts_list'),
    path('posts/<int:id>' , views.PostDetail.as_view() , name='post'),
    path('comments/add/<int:id>' , views.CreateComment.as_view() , name='add_comment'),
    path('comments/edit/<int:id>' , views.EditComment.as_view() , name='edit_comment'),
    path('comments/delete/<int:id>' , views.DeleteComment.as_view() , name='delete_comment'),
]