from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(verbose_name=_('name'), max_length=20, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'],
                name='unique_category_name_slug'
            )
        ]
        ordering = ['name']
