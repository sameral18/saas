from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import BooleanField, ChoiceField, Select


# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300,null=True)
    course_points = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    avg = models.IntegerField(blank=True, null=True)
    collage = models.CharField(max_length=100,blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    mycourse = models.ManyToManyField(Course,blank=True)
    ADMIN = 1
    STUDENT = 2
    WORKER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (WORKER, 'Worker'),

    )
    role = models.PositiveSmallIntegerField(default= STUDENT,choices=ROLE_CHOICES, blank=True, null=True)


class Message(models.Model):
    to=models.ForeignKey(User,on_delete=models.CASCADE)
    msg_from=models.CharField(max_length=100,blank=True, null=True)
    subject=models.CharField(max_length=100,blank=True, null=True)
    message=models.TextField(max_length=250,blank=True, null=True)

