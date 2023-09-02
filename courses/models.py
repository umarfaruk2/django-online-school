from django.db import models
from django.contrib.auth.models import User



class CourseModel(models.Model):
    DEPARTMENT_CHOICES = [
    ('Quality Assurance', 'Quality Assurance'),
    ('Technology and IT', 'Technology and IT'),
    ('Research and Development', 'Research and Development')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=40)
    course_length = models.IntegerField()
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title