from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')
    
    class Meta:
        model = models.Comment
        fields = ('id', 'content', 'user', 'created_at', 'created_updated_at', 'user_id', 'post')

class PostSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    # coments = CommentSerializer(many=True) # verry hungry for data size
    # comments = serializers.StringRelatedField(many=True) # geriau nenaudoti 
    comments = CommentSerializer(many=True , read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    def get_comment_count(self, obj):
            return obj.comments.count()
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'user', 'created_at', 'created_updated_at', 'user_id', 'comments', 'comment_count')
        
        

