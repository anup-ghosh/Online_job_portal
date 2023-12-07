from django.urls import path
from .views import cv_form, GeneratePdf

app_name = 'cv'

urlpatterns = [
    path('cv-form/', cv_form, name='cv_form'),
    path('cv-preview/', GeneratePdf.as_view(), name='cv_preview'),
    path('cv-pdf/', GeneratePdf.as_view(), name='generate_pdf'),
]
