from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from OnlineTrainingPortal.userAuthentication.decorators import admin_required
from OnlineTrainingPortal.course.models import Course,EnrollData,EnrollForm
from OnlineTrainingPortal.blog.models import BlogPostModel
from OnlineTrainingPortal.userAuthentication.models import User

decorators = [login_required,admin_required]


@method_decorator(decorators,name='dispatch')
class AdminSiteView(TemplateView):
    template_name = "administration/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        total_course = Course.objects.all().count()
        total_post = BlogPostModel.objects.all().count()
        total_user = User.objects.all().count()
        total_pending = User.objects.filter(is_approved=False).count()
        course_user = EnrollData.objects.all().count()
        enroll_request = EnrollForm.objects.all().count()
        context['total_course'] = total_course
        context['total_post'] = total_post
        context['total_user'] = total_user
        context['total_pending'] = total_pending
        context['course_user'] = course_user
        context['enroll_request'] = enroll_request
        return context



