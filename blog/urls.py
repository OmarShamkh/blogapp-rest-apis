from django.urls import path
from . import views

urlpatterns = [
    path('posts/' , views.PostList.as_view() , name='posts_list'),
    path('posts/<int:id>' , views.PostDetail.as_view() , name='post'),
    path('comments/<int:id>' , views.Comments.as_view() , name='comment'),
    path('admin/posts/<int:id>' , views.AdminPostDetail.as_view() , name='admin_post'),
]