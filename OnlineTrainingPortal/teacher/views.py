from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from OnlineTrainingPortal.userAuthentication.decorators import teacher_required
from OnlineTrainingPortal.course.models import CoursePermissionModel
from OnlineTrainingPortal.course.models import CourseModule

@method_decorator(login_required,name='dispatch')
@method_decorator(teacher_required, name='dispatch')
class TeacherHomeView(TemplateView):
    template_name = 'teacher/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        permission_course = CoursePermissionModel.objects.filter(teacher_id = self.request.user.id)
        context['permission_course_list'] = permission_course
        return context
