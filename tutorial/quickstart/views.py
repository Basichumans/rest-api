from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.exceptions import ValidationError
from . import models, serializers


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   #read only when not logged in, and logged in when logged in
    
    def perform_create(self, serializer):            
        serializer.save(user=self.request.user)
        


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   #read only when not logged in, and logged in when logged in
   
   

   
   
    def delete(self, request, *args, **kwargs):
        post = models.Post.objects.filter(pk=kwargs['pk'], user=request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)                         
        else:
            raise ValidationError('You can only delete your own posts')
        
    
    
    
    def perform_create(self, serializer):            
        serializer.save(user=self.request.user)
            

    def put(self, request, *args, **kwargs):
       post = models.Post.objects.filter(pk=kwargs['pk'], user=request.user)
       if post.exists() or request.user.is_superuser:                        #  superuser, can edit any post
           return self.update(request, *args, **kwargs)
       else:
           raise ValidationError('You can only update your own posts')
       
       
       
class CommentList(generics.ListCreateAPIView):
    # queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   #read only when not logged in, and logged in when logged in
    
    def perform_create(self, serializer):
        post = models.Post.objects.get(pk=self.kwargs['pk'])            
        serializer.save(user=self.request.user)
        
    
    def get_queryset(self):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        return models.Comment.objects.filter(post=post)