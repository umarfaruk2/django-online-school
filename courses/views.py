from django.shortcuts import render, redirect
from .forms import CourseModelForm
from django.views.generic.edit import FormView


class CourseView(FormView):
    template_name = 'course/create_course.html'
    form_class = CourseModelForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        return redirect('create_course')