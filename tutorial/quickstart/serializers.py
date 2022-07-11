from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'user', 'created_at', 'created_updated_at', 'user_id')
        
        
