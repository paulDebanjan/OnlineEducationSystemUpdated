from django.shortcuts import render
from .models import MessageModel, GroupModel
# Create your views here.

def message_view(request,group_name):
    group = GroupModel.objects.filter(group_name = group_name).first()

    if group:
        messages = MessageModel.objects.filter(group_name = group)
    else:
        group = GroupModel(group_name = group_name)
        group.save()
    return render(request,'message/message.html',{'group_name' : group_name,'messages':messages})
