from django import forms
from .models import Post, Like

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class LikeCreationForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post_id','user_id']
    
    def is_valid(self):
        like = list(Like.objects.filter(post_id=self.data['post_id'] , user_id=self.data['user_id']))
        if like:
            return False
        return True