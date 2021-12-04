from django.views import generic

from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/home.html'
    queryset = Post.objects.published_posts()
    paginate_by = 20
