from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.DO_NOTHING,
        related_name='articles_written'
    )
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        related_name='articles',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        unique=True
    )
    slug = models.SlugField(blank=True)
    content = models.TextField(unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    is_hidden = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} just created a {self.title}'
