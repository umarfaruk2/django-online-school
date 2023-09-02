from django.db import models
from django.contrib.auth.models import User
from .contains import DEPARTMENT
import uuid


class CourseCreateModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    department = models.CharField(choices=DEPARTMENT, max_length=40)
    course_length = models.IntegerField()
    images = models.ImageField(upload_to='images/course')
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title