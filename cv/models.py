from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.IntegerField()

class Experience(models.Model):
    job_title = models.CharField(max_length=100,null=True, blank=True)
    company = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True,default="")
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True,default="")
