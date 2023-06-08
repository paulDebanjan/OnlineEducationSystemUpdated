from signal import default_int_handler
from django.urls import reverse
from django.db import models
# from tinymce.models import HTMLField
from autoslug import AutoSlugField
    

class BlogPostModel(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True,blank=True)
    notice_file = models.FileField (upload_to='notice/',max_length=250,null=True,default=None,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = AutoSlugField("Post Address", unique=True, always_update=False, populate_from="title")
    
    def get_absolute_url(self):
        return reverse("notice:adminBlog")
    