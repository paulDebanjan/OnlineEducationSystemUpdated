from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _




class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=25)
    desc_text = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='profile_img/',max_length=250,null=True,default=None)

    def __str__(self):
        return self.user.first_name
    

# Create your models here.


# class StudentManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

# class TeacherManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)
# class AdminManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


# class User(AbstractUser):

#     class Types(models.TextChoices):
#         STUDENT = "student","Student"
#         TEACHER = "teacher","Teacher"
#         ADMIN = "admin","Admin"

#     type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.STUDENT)
    
#     def get_absolute_url(self):
#         # return reverse("users:page", kwargs={"username": self.username})
#         return reverse("home")

# class StudentMore(models.Model):
#     class Depertments(models.TextChoices):
#         SWE = "swe","Software Enginnering"
#         CSE = "cse","Computer Science Engineering"
#         EEE = "eee","Electrical and Electronic Engineering"

#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     depertment = models.CharField(_('Depertment'), max_length=70 ,choices=Depertments.choices)


# class Student(User):
#     base_type = User.Types.STUDENT
#     # objects = StudentManager()
#     @property
#     def more(self):
#         return self.studentmore
#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.type = User.Types.STUDENT
#         return super().save(*args, **kwargs)


# class TeacherMore(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     qualification = models.CharField(_('Qualification'), max_length=150, blank=True)


# class Teacher(User):
#     base_type = User.Types.TEACHER
#     # objects = TeacherManager()

#     @property
#     def more(self):
#         return self.teachermore

#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.type = User.Types.TEACHER
#         return super().save(*args, **kwargs)

# class AdminMore(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     address = models.CharField(_('Address'), max_length=150, blank=True)


# class Admin(User):
#     base_type = User.Types.ADMIN
#     objects = AdminManager()

#     @property
#     def more(self):
#         return self.adminmore

#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.type = User.Types.ADMIN
#         return super().save(*args, **kwargs)