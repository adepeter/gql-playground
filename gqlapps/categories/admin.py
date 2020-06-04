from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'parent']
    prepopulated_fields = {
        'slug': ('name',),
    }
    ordering = ['name', 'parent']
