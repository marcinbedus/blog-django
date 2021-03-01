from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("created_by", "content", "post")
        widgets = {
            'created_by': forms.HiddenInput(),
            'post': forms.HiddenInput(),
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "content", "created_by", "image")
        widgets = {
            'created_by': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }