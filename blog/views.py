import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from django.shortcuts import Http404
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Post


class HomeView(generic.ListView):
    template_name = 'blog/home.html'
    queryset = Post.objects.published_posts()
    ordering = ['-published_at']
    paginate_by = 10

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


@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(login_required, name="dispatch")
class AdminUploadImageView(generic.View):
    def post(self, request):
        if not request.user.is_admin:
            return JsonResponse(
                {
                    'error': 'Not privileged enough.'
                },
                status=403,
            )

        image = request.FILES.get('file')
        image_types = [
            'image/png', 'image/jpg',
            'image/jpeg', 'image/pjpeg', 'image/gif'
        ]
        if image.content_type not in image_types:
            return JsonResponse(
                {
                    'error': 'Bad image format.'
                },
                status=400,
            )

        storage = FileSystemStorage()
        path = storage.save(os.path.join('images', image.name), image)
        url = storage.url(path)

        return JsonResponse(
            {
                'location': url,
            }
        )
