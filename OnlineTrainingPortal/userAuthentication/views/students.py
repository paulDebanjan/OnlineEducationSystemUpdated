from django.views.generic import CreateView
from ..models import User
from ..forms import StudentSignUpForm
from django.shortcuts import redirect 
from django.contrib.auth import login

# from ..models import Student

# class StudentSignUpView(CreateView):
#     model = Student
#     fields = ['first_name','last_name','username','email','password']
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    
    template_name = 'userAuthentication/student_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

