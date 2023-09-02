from django import forms
from .models import CourseModel


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = ['title', 'department', 'course_length', 'description']