from django.contrib import admin
from .models import CourseModel

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'course_length', 'department', 'description', 'created_at', 'updated_at')
