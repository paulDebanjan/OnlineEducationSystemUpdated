from django.urls import path

from . import views


app_name = "enquiry"
urlpatterns = [
    path(
        route='',
        view=views.EnquiryView.as_view(),
        name='enquiryForm'
    ),
]