from django.contrib import admin
from .models import BlogPostModel


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','description')

admin.site.register(BlogPostModel,BlogPostAdmin)