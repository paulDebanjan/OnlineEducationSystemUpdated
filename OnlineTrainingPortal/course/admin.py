from django.contrib import admin
from .models import Course, CourseSchedule, CoursePermissionModel, CourseModule, CourseMaterial, Question,EnrollData,EnrollForm, Answer

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(EnrollData)
admin.site.register(EnrollForm)
admin.site.register(CourseModule)
admin.site.register(CourseSchedule)
admin.site.register(CourseMaterial)
admin.site.register(CoursePermissionModel)