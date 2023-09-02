from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout')
]
