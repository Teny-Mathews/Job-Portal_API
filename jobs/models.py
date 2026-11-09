from django.db import models
from accounts.models import CustomUser

class Job(models.Model):
    job_title=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    job_description=models.TextField()
    location=models.CharField(max_length=20)
    salary=models.DecimalField( max_digits=10,decimal_places=2)
    jobtype_choice=[('onsite','Onsite'),('remote','Remote'),('hybrid','Hybrid')]
    job_type=models.CharField(max_length=20,choices=jobtype_choice)
    posted_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
