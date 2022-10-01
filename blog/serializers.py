from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id' ,'title', 'content', 'published_date')
        ordering = ['-published_date']
    

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user','post', 'content', 'published_date')
        ordering = ['-published_date']


class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content']
