from rest_framework import status
from rest_framework.request import Request 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from blog import serializers
from .models import Post, Comment
# Create your views here.


class PostList(APIView):
    # any user can see all posts
    permission_classes = [AllowAny]
    def get(self, request):
        """
        List all the posts.
        """ 
        posts = Post.objects.order_by('-published_date')
        serializer = serializers.PostSerializer(posts , many=True)

        return Response(serializer.data)



class PostDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request:Request, id):
        """
        Get post with its connected comments.
        """ 
        try:
            post = Post.objects.get(id=id)
            comments = post.comments.order_by('-published_date')
            serializer = serializers.PostSerializer(post)
            new_serializer = serializer.data
            new_serializer['comments'] = list(comments.values())
            return Response(new_serializer , status= status.HTTP_200_OK)

        except Post.DoesNotExist:
            message = {"Post dosen't exist"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
    


class Comments(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request:Request, id):
        comment = Comment.objects.get(id=id)
        serializer = serializers.CommentSerializer(comment)
        return Response(serializer.data , status= status.HTTP_200_OK)
        
    def post(self, request:Request, id):
        """
        Create a comment on a post
        """
        post = Post.objects.get(id=id)
        username = request.user.username
        comment = Comment.objects.create(
            user =request.user,
            user_name = username,
            post =post,
            content=request.data['content']
        )
        comment.save()
        message = {"Comment created successfully"}
        return Response(message , status=status.HTTP_201_CREATED)
    
    
    def put(self, request:Request, id):
        """
        Edit comment
        """
        comment = Comment.objects.get(id=id)
        if request.user == comment.user:
            serializer = serializers.CreateCommentSerializer(instance=comment , data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"Comment updated successfully"}
                return Response(message,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request:Request, id):
        """
        Delete comment
        """
        comment = Comment.objects.get(id=id)

        if request.user == comment.user:
            comment.delete()
            message = {"Comment deleted successfully"}

            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AdminPostDetail(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request:Request, id):
        """
        Create a new post
        """
        post = Post.objects.create(
            user =request.user,
            title = request.data['title'],
            content=request.data['content']
        )
        post.save()
        message = {"Post created successfully"}
        return Response(message , status=status.HTTP_201_CREATED)

    def put(self, request:Request, id):
        """
        Edit post
        """
        post = Post.objects.get(id=id)
        if request.user == post.user:
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            message = {"Post updated successfully"}
            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id):
        """
        Delete post
        """
        post = Post.objects.get(id=id)

        if request.user == post.user:
            post.delete()
            message = {"Post deleted successfully"}

            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


        