from django.contrib import admin
from .models import MessageModel, GroupModel


# Register your models here.
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id','message','created','group_name']


admin.site.register(MessageModel,MessageModelAdmin)


class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'created', 'updated']

admin.site.register(GroupModel,GroupModelAdmin)