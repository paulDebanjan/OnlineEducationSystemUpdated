from traceback import print_tb
from channels.consumer import SyncConsumer,AsyncConsumer
from .models import MessageModel, GroupModel
from OnlineTrainingPortal.userAuthentication.models import User
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from time import sleep
import asyncio
import json



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected...',event)
        print('Channel layer...', self.channel_layer)
        print('Channel name...', self.channel_name)                                         # print group name which is collected from routing path
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
            )

        self.send({
            'type' : 'websocket.accept'
        })
    def websocket_receive(self,event):
        print('websocket connected...',event['text'])
        print(type(event['text']))
        data = json.loads(event['text'])
        print(data['user_id'])
        group = GroupModel.objects.get(group_name = self.group_name)
        user_id = User.objects.get(pk = data['user_id'])
        print(user_id)
        message = MessageModel(message = data['msg'],group_name = group, user_id=user_id)
        message.save()


        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
            'type' : 'msg.message',
            'message' : event['text'],
            'user_id': data['user_id']
            })

    def msg_message(self,event):
        print('accual data',event['message'])
        self.send({
            'type' : 'websocket.send',
            'text' : event['message'],
            'user_id': event['user_id']
        })

    def websocket_disconnect(self,event):
        print('websocket connected...',event)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
            )
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connected...',event)
        print('Channel layer...', self.channel_layer)
        print('Channel name...', self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
            )

        await self.send({
            'type' : 'websocket.accept'
        })
    async def websocket_receive(self,event):
        print('websocket connected...',event['text'])
        print(type(event['text']))
        data = json.loads(event['text'])
        print(data['msg'])
        group = await database_sync_to_async(GroupModel.objects.get)(group_name = self.group_name)
        message = MessageModel(
            message = data['msg'],
            group_name = group,
            user_id = self.user.pk
            )
        await database_sync_to_async (message.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
            'type' : 'msg.message',
            'message' : event['text']
            })

    async def msg_message(self,event):
        print('accual data',event['message'])
        await self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    async def websocket_disconnect(self,event):
        print('websocket connected...',event)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
            )
        raise StopConsumer()


