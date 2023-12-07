# cv/forms.py
from django import forms
from .models import PersonalInfo, Education, Experience

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        widgets = {
            'profile_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
