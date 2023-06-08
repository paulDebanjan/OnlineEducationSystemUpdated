from cgitb import handler
from django.db import router
from django.urls import path
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_view
from .views import classroom,students,teachers
from .views.classroom import Error500View as error500
from .views.classroom import Error400View as error400


app_name = "userAuthentication"
urlpatterns = [
    path(
        route='',
        view=classroom.SignUpView.as_view(),
        name='singup'
    ),
    path(
        route='student/',
        view=students.StudentSignUpView.as_view(),
        name='studentSignUp'
    ),
    path(
        route='teacher/',
        view=teachers.TeacherSignUpView.as_view(),
        name='teacherSignUp'
    ),
    path(
        route='profile/',
        view=classroom.ProfileTemplateView.as_view(),
        name='profile'
    ),
    path(
        route='login/',
        view=auth_view.LoginView.as_view(template_name='userAuthentication/login.html'),
        name='login'
    ),
    path(
        route='logout/',
        view=auth_view.LogoutView.as_view(template_name='index.html'),
        name='logout'
    ),
    path(
        route='password_change/',
        view=auth_view.PasswordChangeView.as_view(success_url=reverse_lazy('userAuthentication:password_change_done'),template_name='userAuthentication/password_change.html'),
        name='password_change'
    ),
    path(
        route='password_change/done/',
        view=auth_view.PasswordChangeDoneView.as_view(template_name='userAuthentication/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        route='password_reset/',
        view=classroom.ResetPasswordView.as_view(),
        name='password_reset'

    ),
    path(
        route='password_reset/done',
        view=auth_view.PasswordResetDoneView.as_view(template_name='userAuthentication/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        route='reset/<uidb64>/<token>/',
        view=auth_view.PasswordResetConfirmView.as_view(template_name='userAuthentication/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        route='reset/done/',
        view=auth_view.PasswordResetCompleteView.as_view(template_name='userAuthentication/password_reset_done.html'),
        name='password_reset_complete'
    ),
    path(
        route='settings/',
        view=classroom.SettingsView.as_view(),
        name='settings'
    ),
    path(
        'unApproved/',classroom.unApprovedPage,name='unApproved'
    ),
    path(
        route='userPendingView/',
        view=classroom.AdminUserPendingView.as_view(),
        name='userPendingView'
    ),
    path(
        route='course_request/',
        view=classroom.CoursePendingView.as_view(),
        name='course_request'
    ),
    path(
        route='createuser/',
        view=classroom.AdminCreateUser.as_view(),
        name='createUser'
    ),
    path(
        route='approved/<int:pk>/',
        view=classroom.ApprovedView.as_view(),
        name='approved'
    ),
    path(
        route='course_approved/<int:pk>/',
        view=classroom.CourseApprovedView.as_view(),
        name='course_approved'
    ),
    path(
        route='course_permission_delete/<int:pk>/',
        view=classroom.CourseDeleteView.as_view(),
        name='course_permission_delete'
    ),
    path(
        route='delete_user/<int:pk>/',
        view=classroom.DeleteUserView.as_view(),
        name='delete_user'
    ),
]
