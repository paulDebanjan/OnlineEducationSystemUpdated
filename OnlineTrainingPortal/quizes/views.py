from django.shortcuts import render
# from django.views.generic.list import ListView
# from .models import Question,Answer

# # @method_decorator(teacher_decorators_list,name='dispatch')
# class QuestionListView(ListView):
#     model = Question
    

#     def get_queryset(self):
#         material_object = CourseMaterial.objects.get(slug = self.kwargs['slug3'])
#         return Question.objects.filter(material_id = material_object.id)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         element = CourseMaterial.objects.get(slug = self.kwargs['slug3'])
#         print(element.slug)
        
#         context['element_id'] = element.id
#         context['element_slug'] = element.slug
#         context['course_slug'] = self.kwargs['slug']
#         context['module_slug'] = self.kwargs['slug2']
#         context['permission_course_list'] = CoursePermissionModel.objects.filter(teacher_id = self.request.user.id)
#         return context
