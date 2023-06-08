from django.db import models

# Create your models here.
class Enquiry(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField(max_length=250)
    enquiry_specification = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
