from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),                # all posts
    path('posts/<int:pk>/', views.PostDetail.as_view()),     # single post int:pk for id of post 
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),          # all comments
]