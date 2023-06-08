from django.views.generic import CreateView
from ..models import User
from ..forms import TeacherSignUpForm
from django.shortcuts import redirect 
from django.contrib.auth import login
# from ..models import Teacher

# class TeacherSignUpView(CreateView):
#     model = Teacher
#     fields = ['username','email','password']

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'userAuthentication/teacher_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')