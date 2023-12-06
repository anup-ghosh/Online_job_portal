from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20) 
    email = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skills = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    def _str_(self):
        return  self.user.username

class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    def _str_(self):
        return  self.user.username
    
class Recruiter(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    company=models.CharField(max_length=1000,null=True)
    type=models.CharField(max_length=15,null=True)
    status = models.CharField(max_length=20, null=True)
    def _str_(self):
        return  self.user.username

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=20)
    image = models.FileField()
    description = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()
    def _str_(self):
        return  self.title

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    def _str_(self):
        return  self.id