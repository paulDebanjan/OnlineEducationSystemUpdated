from django.db import models
# from OnlineTrainingPortal.userAuthentication.models import User
# from OnlineTrainingPortal.course.models import Course, CourseModule,CourseMaterial

# class Quiz(models.Model):
#     name = models.CharField(max_length=120)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     module = models.ForeignKey(CourseModule, on_delete=models.CASCADE)
#     number_of_questions = models.IntegerField()
#     time = models.IntegerField(help_text="duration of the quiz in minutes")

#     def __str__(self):
#         return f"{self.name}-{self.module}-{self.course}"
    
#     def get_questions(self):
#         return self.question_set.all()
#     class Meta:
#         verbose_name_plural = 'Quizes'


# class Question(models.Model):
#     text = models.CharField(max_length=150)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     # material_id = models.ForeignKey(CourseMaterial,on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.text}"

#     def get_answers(self):
#         return self.answer__set.all()

# class Answer(models.Model):
#     text = models.CharField(max_length=150)
#     correct = models.BooleanField(default=False)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


# class Result(models.Model):
#     quiz = models.ForeignKey(CourseMaterial, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.FloatField()

#     def __str__(self):
#         return str(self.pk) 