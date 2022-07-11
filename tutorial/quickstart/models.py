from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(_('title'),max_length=150)
    content = models.TextField(_('content'))
    user  = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'))
    created_at= models.DateTimeField(_('created at'), auto_now_add=True,)
    created_updated_at= models.DateTimeField(_('created at'), auto_now=True,) 
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'), related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'), related_name='comments')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True,)
    created_updated_at = models.DateTimeField(_('created at'), auto_now=True,)
    content = models.TextField(_('content'))


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'), related_name='likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name=_('user'), null=True, blank=True, related_name='likes')
   


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name=_('comment'), related_name='comment_likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name=_('user'),null=True, blank=True)
