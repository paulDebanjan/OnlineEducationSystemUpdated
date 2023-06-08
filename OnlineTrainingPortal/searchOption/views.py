from django.shortcuts import render
from course.models import Course

# Create your views here.
# def searchOption(request):
#     courselist = Course.objects.all().order_by('-updated')
#     sp = ''
#     if request.method == 'GET':
#         sb = request.GET.get('search_box')
#         if sb != None:
#             courselist = Course.objects.filter(course_title__icontains = sb)


#     data = {
#         'search' : sp,
#         'courselist' : courselist,
#     }
#     return render(request, 'course/course.html', data)
