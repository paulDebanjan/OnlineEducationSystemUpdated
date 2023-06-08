from datetime import date
from django.urls import reverse,reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect,render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.forms import inlineformset_factory
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from OnlineTrainingPortal.userAuthentication.decorators import teacher_required,student_required, admin_required, teacher_course_assign_required
from .models import Answer, Course, CourseSchedule, CoursePermissionModel, CourseModule, CourseMaterial, Question, Answer, EnrollForm, EnrollData
# from OnlineTrainingPortal.quizes.models import 
from .forms import BaseAnswerInlineFormSet, QuestionForm
from django.http import JsonResponse 

admin_decorators_list = [login_required,admin_required]
teacher_decorators = [login_required,teacher_required]
teacher_decorators_list = [login_required,teacher_required, teacher_course_assign_required]

student_decorators_list = [login_required,student_required]



# For all type user
class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        course = Course.objects.get(slug = self.kwargs['slug'])
        schedules = CourseSchedule.objects.filter(course_id = course.id)
        dateToday = date.today()
        module_list = CourseModule.objects.filter(course_id = course.id)
        module_material = CourseMaterial.objects.filter(course_id = course.id)
        context['course_slug'] = self.kwargs['slug']
        context['schedules'] = schedules
        count = 0
        user_pk = self.request.user.pk
        enroll_found = EnrollData.objects.filter(user_id = user_pk, course_id= course)
        enoll_form_active = True
        for schedule in schedules:
            if schedule.start_date > date.today():
                count += 1
                break;
        context["total_schedule"] = count
        context['dateToday'] = dateToday
        context['module_list'] = module_list
        if (enroll_found.count() == 1):
            enoll_form_active = False
            context['module_material'] = module_material
        else:
            enoll_form_active = True
        context["enoll_form_active"] = enoll_form_active
        return context
 
    
# For Admin User
@method_decorator(admin_decorators_list,name='dispatch')
class CourseCreateView(CreateView):
    model=Course
    # form_class = CourseForm
    fields= ['title','video','topic','description','lesson','duration']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Course"
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


@method_decorator(admin_decorators_list,name='dispatch')
class CourseUpdateView(UpdateView):
    model=Course
    # form_class = CourseForm
    fields= ['title','video','topic','description','lesson','duration']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Course"
        return context

@method_decorator(admin_decorators_list,name='dispatch')   
class CourseDeleteView(DeleteView):
    model=Course
    success_url = reverse_lazy('course:adminCourseList')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        course = Course.objects.get(slug = self.kwargs['slug'])
        context['course_title'] = course.title
        return context



@method_decorator(admin_decorators_list,name='dispatch')
class PermissionListView(ListView):
    model = CoursePermissionModel

    def get_queryset(self):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        return CoursePermissionModel.objects.filter(course_id=course_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slug = self.kwargs['slug']
        context['slug_text'] = slug
        course = Course.objects.get(slug = self.kwargs['slug'])
        context['course_name'] = course.title
        return context


@method_decorator(admin_decorators_list,name='dispatch')
class PermissionCreateView(CreateView):
    model = CoursePermissionModel
    fields = ['teacher_id']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Permission"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:permissionList', args=[self.kwargs['slug']])

    def form_valid(self, form):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        form.instance.course_id = course_id
        return super().form_valid(form)
    

@method_decorator(admin_decorators_list,name='dispatch')
class PermissionUpdateView(UpdateView):
    model = CoursePermissionModel
    fields = ['teacher_id']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Permission"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:permissionList', args=[self.kwargs['slug']])


@method_decorator(admin_decorators_list,name='dispatch')
class PermissionDeleteView(DeleteView):
    model = CoursePermissionModel

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:permissionList', args=[self.kwargs['slug']])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        permission = CoursePermissionModel.objects.get(id = self.kwargs['pk'])
        slug = self.kwargs['slug']  
        context['slug_text'] = slug
        context['teacher_name'] = permission.teacher_id.first_name+" "+permission.teacher_id.last_name
        context['course_name'] = permission.course_id.title
        return context


@method_decorator(admin_decorators_list,name='dispatch')
class AdminCourseList(ListView):
    model = Course
    template_name = 'course/adminCourse_list.html'


@method_decorator(admin_decorators_list,name='dispatch')
class CourseScheduleCreateView(CreateView):
    model = CourseSchedule
    fields= ['batch_name','start_date','finish_date','start_time','finish_time','weeked_type']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Course Schedule"
        return context

    def form_valid(self, form):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        form.instance.course_id = course_id
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:scheduleList', args=[self.kwargs['slug']])


@method_decorator(admin_decorators_list,name='dispatch')
class CourseScheduleUpdateView(UpdateView):
    model = CourseSchedule
    fields= ['batch_name','start_date','finish_date','start_time','finish_time','weeked_type']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Course Schedule"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:scheduleList', args=[self.kwargs['slug']])


@method_decorator(admin_decorators_list,name='dispatch')
class CourseScheduleDeleteView(DeleteView):
    model = CourseSchedule

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:scheduleList', args=[self.kwargs['slug']])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        schedule = CourseSchedule.objects.get(id = self.kwargs['pk'])
        slug = self.kwargs['slug']  
        context['slug_text'] = slug
        context['batch_name'] = schedule.batch_name
        context['course_name'] = schedule.course_id.title
        return context


@method_decorator(admin_decorators_list,name='dispatch')
class CourseScheduleList(ListView):
    model=CourseSchedule

    def get_queryset(self):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        return CourseSchedule.objects.filter(course_id=course_id)
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        course = Course.objects.get(slug = self.kwargs['slug'])
        context['course_name'] = course.title
        slug = self.kwargs['slug']
        context['slug_text'] = slug
        return context



#Teacher Course Permission Views
@method_decorator(teacher_decorators_list,name='dispatch')
class ModuleListView(ListView):
    model = CourseModule
    def get_queryset(self):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        return CourseModule.objects.filter(course_id=course_id)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        course = Course.objects.get(slug = self.kwargs['slug'])
        permisssion_course = CoursePermissionModel.objects.filter(teacher_id = self.request.user.id)
        context['course_name'] = course.title
        slug = self.kwargs['slug']
        context['slug_text'] = slug
        context['permission_course_list'] = permisssion_course
        return context


@method_decorator(teacher_decorators_list,name='dispatch')
class CreateModuleView(CreateView):
    model = CourseModule
    fields=['name']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Module"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:module_list', args=[self.kwargs['slug']])

    def form_valid(self, form):
        course_id = Course.objects.get(slug = self.kwargs['slug'])
        form.instance.course_id = course_id
        form.instance.creator = self.request.user
        return super().form_valid(form)


@method_decorator(teacher_decorators_list,name='dispatch')
class UpdateModuleView(UpdateView):
    model = CourseModule
    fields=['name']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Module"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:module_list', args=[self.kwargs['slug']])

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


@method_decorator(teacher_decorators_list,name='dispatch')
class DeleteModuleView(DeleteView):
    model = CourseModule

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:module_list', args=[self.kwargs['slug']])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        module = CourseModule.objects.get(id = self.kwargs['pk'])
        slug = self.kwargs['slug']  
        context['slug_text'] = slug
        context['module_name'] = module.name
        return context


@method_decorator(teacher_decorators_list,name='dispatch')
class ModuleElementListView(ListView):
    model = CourseMaterial
    def get_queryset(self):
        course = Course.objects.get(slug = self.kwargs['slug'])
        course_module = CourseModule.objects.get(slug = self.kwargs['slug2'])
        return CourseMaterial.objects.filter(course_id=course.id, module_id=course_module.id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        course = Course.objects.get(slug = self.kwargs['slug'])
        module = CourseModule.objects.get(slug = self.kwargs['slug2'])
        context['course_name'] = course.title
        context['course_slug'] = self.kwargs['slug']
        context['module_slug'] = self.kwargs['slug2']
        context['module_name'] = module.name
        context['permission_course_list'] = CoursePermissionModel.objects.filter(teacher_id = self.request.user.id)
        return context


@method_decorator(teacher_decorators_list,name='dispatch')
class MaterialCreateView(CreateView):
    model = CourseMaterial
    fields = ['name','data','topic','time','number_of_questions']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Material"
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:element_list', args=[self.kwargs['slug'],self.kwargs['slug2']])

    def form_valid(self, form):
        course = Course.objects.get(slug= self.kwargs['slug'])
        form.instance.course_id = course
        module = CourseModule.objects.get(slug=self.kwargs['slug2'])
        form.instance.module_id = module
        form.instance.creator = self.request.user
        return super().form_valid(form)


@method_decorator(teacher_decorators_list,name='dispatch')
class MaterialUpdateView(UpdateView):
    model = CourseMaterial
    fields = ['name','data','topic','time','number_of_questions']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Material"
        return context


    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:element_list', args=[self.kwargs['slug'],self.kwargs['slug2']])

    

# class MaterialUpdateView(UpdateView):
#     model = CourseMaterial
#     fields = ['name','data','topic']

#     def get_success_url(self, *args, **kwargs):
#         return reverse_lazy('course:element_list', args=[self.kwargs['slug'],self.kwargs['pk']])

#     def form_valid(self, form):
#         course = Course.objects.get(slug = self.kwargs['slug'])
#         form.instance.course_id = course.id
#         module = CourseModule.objects.get(slug = self.kwargs['slug2'])
#         form.instance.module_id = module.id
#         form.instance.creator = self.request.user
#         return super().form_valid(form)


@method_decorator(teacher_decorators_list,name='dispatch')
class MaterialDeleteView(DeleteView):
    model = CourseMaterial

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:element_list', args=[self.kwargs['slug'],self.kwargs['slug2']])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        element = CourseMaterial.objects.get(id = self.kwargs['pk'])
        context['element_name'] = element.name
        context['course_slug'] = self.kwargs['slug']
        context['module_slug'] = self.kwargs['slug2']
        return context


@method_decorator(teacher_decorators_list,name='dispatch')
class QuestionListView(ListView):
    model = Question
    

    def get_queryset(self):
        material_object = CourseMaterial.objects.get(slug = self.kwargs['slug3'])
        return Question.objects.filter(material_id = material_object.id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        element = CourseMaterial.objects.get(slug = self.kwargs['slug3'])
        context['element_id'] = element.id
        context['element_slug'] = element.slug
        context['course_slug'] = self.kwargs['slug']
        context['module_slug'] = self.kwargs['slug2']
        context['permission_course_list'] = CoursePermissionModel.objects.filter(teacher_id = self.request.user.id)
        return context


@method_decorator(teacher_decorators_list,name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    template_name = "one_template/form.html"
    fields=['text']
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:question_list', args=[self.kwargs['slug'],self.kwargs['slug2'],self.kwargs['slug3']],)

    def form_valid(self, form):
        material = CourseMaterial.objects.get(slug= self.kwargs['slug3'])
        form.instance.material_id = material
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # element = CourseMaterial.objects.get(id = self.kwargs['pk'])
        # context['element_name'] = element.name
        # context['course_slug'] = self.kwargs['slug']
        context['button_topic'] = "Question"
        return context


@login_required
@teacher_required
def question_change(request, slug,slug2, slug3, question_pk):

    material_slug =CourseMaterial.objects.get(slug=slug3)
    quiz_pk=material_slug.id
    quiz = get_object_or_404(CourseMaterial, pk=quiz_pk)
    question = get_object_or_404(Question, pk=question_pk, material_id=quiz)

    AnswerFormSet = inlineformset_factory(
        Question,
        Answer,
        formset=BaseAnswerInlineFormSet,
        fields=('text', 'is_correct'),
        min_num=2,
        validate_min=True,
        max_num=4,
        validate_max=True
    )

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = AnswerFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, 'Question and answers saved with success!')
            return redirect('course:question_list',slug,slug2,slug3)
    else:
        form = QuestionForm(instance=question)
        formset = AnswerFormSet(instance=question)

    return render(request, 'teacher/question_change_form.html', {
        'quiz': quiz,
        'question': question,
        'form': form,
        'formset': formset
    })

@method_decorator(student_decorators_list,name='dispatch')
class StudenEnrolFormView(CreateView):
    model=EnrollForm
    fields = ['schedule','phone_number']
    template_name="form.html"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('course:detailView', args=[self.kwargs['slug']])

    def form_valid(self, form):
        course = Course.objects.get(slug= self.kwargs['slug'])
        form.instance.user_id = self.request.user
        form.instance.course_id = course
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # element = CourseMaterial.objects.get(id = self.kwargs['pk'])
        # context['element_name'] = element.name
        # context['course_slug'] = self.kwargs['slug']
        context['action'] = "Request"
        context['form_title'] = "Enrolment"
        context['button_topic'] = "Enrollment Request"
        return context
    

def quiz_view(request,pk):
    quiz = CourseMaterial.objects.get(pk = pk)
    return render(request, "quizes/quiz.html", {"obj":quiz})

def quiz_data_view(request, pk):
    quiz = CourseMaterial.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        "data": questions,
        "time": quiz.time,
    })