from django.contrib import admin

from .forms import PostForm
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('id', 'title', 'title_2', 'short_text', 'published_at', 'is_published', 'author')

    def short_text(self, obj):
        if obj.text:
            return obj.text[:30] + '...'
        else:
            return ''
