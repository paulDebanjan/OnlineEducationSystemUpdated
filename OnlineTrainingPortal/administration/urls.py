
from django.urls import path
from . import views

app_name = "administration"
urlpatterns = [
    path(
        route='',
        view=views.AdminSiteView.as_view(),
        name='home'
    ),
    # path(
    #     route='student/',
    #     view=students.StudentSignUpView.as_view(),
    #     name='studentSignUp'
    # ),
    
]
