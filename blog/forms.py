from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Form class for my Post objects"""

    class Meta:
        model = Post
        fields = ('title', 'text',)
