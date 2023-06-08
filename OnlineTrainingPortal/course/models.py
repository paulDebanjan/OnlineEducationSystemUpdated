from asyncio.windows_events import NULL
from email.policy import default
from http.client import UNAUTHORIZED
from statistics import mode
from OnlineTrainingPortal.userAuthentication.models import User
from django.urls import reverse
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField (upload_to='course/',max_length=250,null=True,default=None,blank=True)
    topic = models.CharField(max_length=150, null = True,blank=True)
    lesson = models.IntegerField()
    duration = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=250,null=True)
    total_article = models.IntegerField(null=True,blank=True)
    access_limit = models.CharField(max_length=100, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    video = models.CharField(max_length=250,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = AutoSlugField("Course Address", unique=True, always_update=False, populate_from="title")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course:adminCourseList")

class CourseSchedule(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_name = models.CharField(max_length=70,null=True)
    start_date = models.DateField(null= True)
    finish_date = models.DateField(null= True)
    start_time = models.TimeField(null= True)
    finish_time = models.TimeField(null= True)
    weeked_type = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = AutoSlugField("Batch Address", unique=True, always_update=False, populate_from="batch_name")
    def __str__(self):
        return self.batch_name

class CoursePermissionModel(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.course_id.title
    

class CourseModule(models.Model):
    name = models.CharField(max_length=255,null=False,default=None)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    slug = AutoSlugField("Material Address", unique=True, always_update=False, populate_from="name")
    def __str__(self):
        return self.name


class CourseMaterial(models.Model):
    class MaterialTopic(models.TextChoices):
        SLIDE = "slide","Slide"
        PDF = "pdf","PDF"
        VIDEO = "video", "Video"
        QUIZ = "quiz","Quiz"

    name = models.CharField(max_length=255, null=False)
    data = models.FileField (upload_to='materials/',max_length=250,null=True,blank=True)
    topic = models.CharField("Material Kind",max_length=12, choices=MaterialTopic.choices, default=None)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    module_id = models.ForeignKey(CourseModule,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    number_of_questions = models.IntegerField(default=0)
    time = models.IntegerField(help_text="Duration of the quiz in minutes", null=True)
    slug = AutoSlugField("Material Address", unique=True, always_update=False, populate_from="name")
    def __str__(self):
        return self.name
    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

class Question(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='quizzes')
    text = models.CharField('Question', max_length=70)
    material_id = models.ForeignKey(CourseMaterial,on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    def get_answers(self):
        return self.answer__set.all()

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='answer')
    text = models.CharField('Answer',max_length=255)
    is_correct = models.BooleanField('Corrent answer', default=False)
    
    def __str__(self):
        return self.text


class Result(models.Model):
    course_material = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk) 

class EnrollForm(models.Model):
    class TranactionOption(models.TextChoices):
        SLIDE = "bkash","BKash"
        PDF = "rocket","Rocket"
        VIDEO = "ucash", "Ucash"

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    transaction_method = models.CharField("Transaction Option", max_length=12, choices=TranactionOption.choices)
    transaction_id = models.CharField(max_length=50,null=True)

    
class EnrollData(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)