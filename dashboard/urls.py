from django.urls import path
from . import views

urlpatterns = [
    path('create_course/', views.create_course, name='create_course'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_course/<int:pk>', views.UpdateCourse.as_view(), name='update_course'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
]

