from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('logout/', views.Logout.as_view()),
    
]