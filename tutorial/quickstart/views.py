from django.shortcuts import render
from rest_framework import generics,permissions
from . import models, serializers


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   #read only when not logged in, and logged in when logged in
    
    def perform_create(self, serializer):            
        serializer.save(user=self.request.user)
        
    