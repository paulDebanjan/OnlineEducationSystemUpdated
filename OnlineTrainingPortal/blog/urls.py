from django.urls import path
from . import views

app_name = "notice"
urlpatterns = [
    path(
        route='',
        view=views.BlogListView.as_view(),
        name='home'
    ),
    path(
        route='details/<slug:slug>/',
        view=views.BlogDetailView.as_view(),
        name='blogDetail'
    ),
    path(
        route='delete/<slug:slug>/',
        view=views.BlogDeleteiew.as_view(),
        name='blogdelete'
    ),
    path(
        route='update/<slug:slug>/',
        view=views.BlogUpdateView.as_view(),
        name='blogUpdate'
    ),
    path(
        route='adminBlog/',
        view=views.AdminSiteBlogView.as_view(),
        name='adminBlog'
    ),
    path(
        route='createPost/',
        view=views.PostCreateView.as_view(),
        name='createPost'
    ),
    # path(
    #     route='teacher/',
    #     view=teachers.TeacherSignUpView.as_view(),
    #     name='teacherSignUp'
    # ),
    # path(
    #     route='profile/',
    #     view=classroom.ProfileTemplateView.as_view(),
    #     name='profile'
    # ),
    # path(
    #     route='error500/',
    #     view=classroom.Error500View.as_view(),
    #     name='error500'
    # ),
]


