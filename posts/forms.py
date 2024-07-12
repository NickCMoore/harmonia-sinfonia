from django import forms
from .models import Post, Comment, Flag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }


class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={'cols': 40, 'rows': 3})
        }
