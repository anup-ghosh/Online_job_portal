from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PersonalInfo, Education, Experience

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Experience)