from django.shortcuts import render, redirect
from .models import CourseCreateModel
from django.views.generic.edit import FormView, UpdateView
from .forms import CourseModelForm
from django.urls import reverse_lazy


def dashboard(request):
    courses = CourseCreateModel.objects.filter(user = request.user)
    return render(request, 'dashboard/dashboard.html', {'course': courses})


def create_course(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('dashboard')
    
    else:
        form = CourseModelForm()
    return render(request, 'dashboard/create_course.html', {'form': form})

class UpdateCourse(UpdateView):
    template_name = 'dashboard/update_course.html'
    model = CourseCreateModel
    form_class = CourseModelForm
    success_url = reverse_lazy('dashboard')
    

def delete_course(request, id):
    course_delete = CourseCreateModel.objects.get(pk = id).delete()

    return redirect('dashboard')