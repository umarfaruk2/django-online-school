from django.contrib import admin
from .models import CourseCreateModel

@admin.register(CourseCreateModel)
class CourseCreateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'course_length', 'department', 'description', 'created_at', 'updated_at')

