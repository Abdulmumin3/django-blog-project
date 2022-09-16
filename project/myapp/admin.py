from django.contrib import admin
from .models import Newsletter

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'publish', 'description',)
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)
# Register your models here.
