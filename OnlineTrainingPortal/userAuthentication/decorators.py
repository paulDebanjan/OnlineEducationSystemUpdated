from django.core.exceptions import PermissionDenied, BadRequest
from django.shortcuts import redirect
from OnlineTrainingPortal.course.models import CoursePermissionModel, Course

# def role_required(allowed_role=[]):
#     def decorator(view_func):
#         def wrap(request, *args, **kwargs):
#             if request.is_student == True:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 raise PermissionDenied
#         return wrap
#     return decorator

def student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_student and request.user.is_approved:
            return function(request, *args, **kwargs)
        else:
            return PermissionDenied
            # return redirect('userAuthentication:error500')
    return wrap
    
def teacher_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_teacher and request.user.is_approved:
            return function(request, *args, **kwargs)
        else:
            return PermissionDenied
            # return redirect('userAuthentication:error500')
    return wrap
    
def teacher_course_assign_required(function):
    def wrap(request, *args, **kwargs):
        try:
            course_id_number = Course.objects.get(slug = kwargs['slug']).id
            if CoursePermissionModel.objects.filter(course_id = course_id_number, teacher_id=request.user.id).count() :
                return function(request, *args, **kwargs)
            else:
                return PermissionDenied
                # return redirect('userAuthentication:error500')
        except:
            return BadRequest   
    return wrap
def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin and request.user.is_approved:
            return function(request, *args, **kwargs)
        else:
            return PermissionDenied
            # return redirect('home')
    return wrap

    