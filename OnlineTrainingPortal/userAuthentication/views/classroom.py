from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import student_required,admin_required, teacher_required
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from ..models import User
from ..forms import AdminSiteUserForm
from OnlineTrainingPortal.course.models import Course, EnrollData, EnrollForm


admin_decorators_list = [login_required,admin_required]


# For all type user
class SignUpView(TemplateView):
    template_name = 'userAuthentication/signup.html'


class Error500View(TemplateView):
    template_name = 'userAuthentication/500.html'

class Error400View(TemplateView):
    template_name = 'userAuthentication/400.html'

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'userAuthentication/password_reset.html'
    email_template_name = 'userAuthentication/password_reset_email.html'
    subject_template_name = 'userAuthentication/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('userAuthentication:password_reset_done')



# For  authenticate user
@method_decorator(login_required,name='dispatch')
# @method_decorator(student_required,name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'


@method_decorator(login_required,name='dispatch')
@method_decorator(teacher_required,name='dispatch')
class TeacherHomePageView(TemplateView):
    template_name = 'userAuthentication/teacher_home.html'
    

@method_decorator(login_required,name='dispatch')
class SettingsView(TemplateView):
    template_name = 'userAuthentication/settings.html'


# @method_decorator(login_required,name='dispatch')
def unApprovedPage(request):
    if request.user.is_teacher:
        if request.user.is_approved:
            return redirect ('teacher:home')
    return render(request,"userAuthentication/notApproved.html")
        


#Admin Side Class
@method_decorator(admin_decorators_list, name='dispatch')
class AdminUserPendingView(ListView):
    model = User
    template_name = 'userAuthentication/userPending_list.html'
    
    def get_queryset(self):
        return User.objects.filter(is_approved=False)


@method_decorator(admin_decorators_list, name='dispatch')
class AdminCreateUser(CreateView):
    model = User
    form_class = AdminSiteUserForm
    def form_valid(self, form):
        user = form.save()
        return redirect('userAuthentication:userPendingView')
    # success_url = reverse_lazy('userAuthentication:userPendingView')


@method_decorator(admin_decorators_list, name='dispatch')
class ApprovedView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['pk'])
        user.is_approved = True
        user.save()
        print(user.is_approved)
        return redirect('userAuthentication:userPendingView')


@method_decorator(admin_decorators_list, name='dispatch')
class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('userAuthentication:userPendingView')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        user = User.objects.get(id = self.kwargs['pk'])
        context['username'] = user.username
        return context



@method_decorator(admin_decorators_list, name='dispatch')
class CoursePendingView(ListView):
    model = EnrollForm
    template_name = 'userAuthentication/coursePermissionPending_list.html'
    

@method_decorator(admin_decorators_list, name='dispatch')
class CourseApprovedView(View):
    def get(self, request, *args, **kwargs):
        course_request = EnrollForm.objects.get(id=self.kwargs['pk'])
        save_data = EnrollData(course_id = course_request.course_id, user_id=course_request.user_id, schedule= course_request.schedule)
        save_data.save()
        course_request.delete()
        return redirect('userAuthentication:course_request')

@method_decorator(admin_decorators_list, name='dispatch')
class CourseDeleteView(View):
    def get(self, request, *args, **kwargs):
        course_request = EnrollForm.objects.get(id=self.kwargs['pk'])
        course_request.delete()
        return redirect('userAuthentication:course_request')


