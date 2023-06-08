from cgitb import handler
from django.db import router
from django.urls import path
from . import views

app_name = "teacher"
urlpatterns = [
    path(
        route='home',
        view=views.TeacherHomeView.as_view(),
        name='home'
    ),
]
