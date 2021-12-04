from django.shortcuts import Http404
from django.views import generic

from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/home.html'
    queryset = Post.objects.published_posts()
    ordering = ['-published_at']
    paginate_by = 20

class PostView(generic.DetailView):
    template_name = 'blog/post.html'

    def get_object(self):
        try:
            post = Post.objects.get(pk=self.kwargs.get('pk'))
            if post.is_published:
                return post
            else:
                raise Http404
        except Post.DoesNotExist:
            raise Http404
