from django import forms
from posts import models

class PostForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = models.Post
        fields = ['message']
