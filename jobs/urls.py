from django.urls import path
from jobs import views

urlpatterns = [
    path('joblistcreate/', views.Joblistcreate.as_view()),
    path('jrud/<int:i>/', views.JobRetrieveUpdateDelete.as_view())
]
