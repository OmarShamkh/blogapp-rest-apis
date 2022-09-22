from mimetypes import common_types
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
        posts = Post.objects.all() 
        serializer = serializers.PostSerializer(posts , many=True)
        return Response({"Posts": serializer.data})



class PostDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request:Request, id):
        """
        Get post with its connected comments.
        """ 
        try:
            post = Post.objects.get(id=id)
           
            """
            Get all comments connected to the post using Indexing.
            CREATE INDEX "blog_comment_post_id" ON "blog_comment" ("post_id")
            """ 
            comments = post.comments.all()
            comments = comments.values()
            serializer = serializers.PostSerializer(post)
            new_serializer = dict(serializer.data)
            new_serializer['comments'] = comments

            return Response(new_serializer , status= status.HTTP_200_OK)

        except Post.DoesNotExist:
            message = {"Post dosen't exist"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
    



class CreateComment(APIView):
    # ONLY authenticated users can create a new comment.
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CreateCommentSerializer

    def post(self, request:Request, id):
        """
        Create a comment on a post
        """
        post = Post.objects.get(id=id)
        comment = Comment.objects.create(
            user =request.user,
            post =post,
            content=request.data['content']
        )
        comment.save()
        message = {"Comment created successfully"}
        return Response(message , status=status.HTTP_201_CREATED)
        
        
class EditComment(APIView):
    # ONLY authenticated users can edit a comment.
    permission_classes = [IsAuthenticated]
    serializer = serializers.CreateCommentSerializer

    def post(self, request:Request, id):
        
        comment = Comment.objects.get(id=id)

        # print("comment user :" ,comment.user)
        # print("request user :" ,request.user)

        if request.user == comment.user:
            new_comment = request.data['content']
            comment.content = new_comment   
            comment.save()

            message = {"Comment Updated successfully"}

            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)



class DeleteComment(APIView):
    # ONLY authenticated users can delete a comment.
    permission_classes = [IsAuthenticated]

    def get(self, request:Request, id):
        comment = Comment.objects.get(id=id)

        if request.user == comment.user:
            comment.delete()
            message = {"Comment deleted successfully"}

            return Response(message,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

        