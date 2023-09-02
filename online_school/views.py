from django.shortcuts import render
from dashboard.models import CourseCreateModel
from dashboard.contains import DEPARTMENT


def home(request):
    search_item = request.GET.get('search')
    course = CourseCreateModel.objects.all() 
    department_search = (request.GET.get('department'))
    
    if department_search:
        course = CourseCreateModel.objects.filter(department__icontains = department_search) 
        print(course)
    if search_item:
       course = CourseCreateModel.objects.filter(title__icontains = search_item) 
    
    department = []

    for item  in DEPARTMENT:
        department.append(item[0])
    
    return render(request, 'home.html', {'course': course, 'department': department})