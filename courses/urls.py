from django.urls import path
from . import views

urlpatterns = [
    path('create_course/', views.CourseView.as_view(), name='create_course')
]
