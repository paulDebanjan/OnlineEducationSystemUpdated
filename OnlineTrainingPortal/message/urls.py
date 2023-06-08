from django.urls import path
from . import views

app_name = "message"
urlpatterns = [
    path(
        route='group/<group_name>/',
        view= views.message_view,
        name = "message"
        )
]