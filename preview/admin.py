from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'meta_description', 'main_description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(BlogPost, BlogPostAdmin)
