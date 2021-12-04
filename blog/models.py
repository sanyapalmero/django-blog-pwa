from django.db import models
from django.utils import timezone
from users.models import User


class BlogQuerySet(models.QuerySet):
    def published_posts(self):
        return self.filter(is_published=True)


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateField(default=timezone.now, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    objects = BlogQuerySet.as_manager()
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
