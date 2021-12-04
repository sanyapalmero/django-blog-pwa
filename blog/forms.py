from django import forms
from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'title_2', 'text', 'published_at', 'is_published', 'author',
        ]
        widgets = {
            'text': TinyMCE(),
        }
