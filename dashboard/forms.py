from django import forms
from .models import CourseCreateModel


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = CourseCreateModel
        fields = ['title', 'department', 'course_length', 'images', 'description']