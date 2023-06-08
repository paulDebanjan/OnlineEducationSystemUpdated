from django.db import models
from OnlineTrainingPortal.userAuthentication.models import User

# Create your models here.
class MessageModel(models.Model):
    message = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    group_name = models.ForeignKey('GroupModel',on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ['-created']

    def __str__(self):
        return self.group_name

class GroupModel(models.Model):
    group_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created','-updated']

    def __str__(self):
        return self.group_name