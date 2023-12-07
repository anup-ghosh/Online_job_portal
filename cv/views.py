from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa 
from .models import PersonalInfo, Education, Experience
from .forms import PersonalInfoForm, EducationForm, ExperienceForm
from django.contrib import messages

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('cv/cv_pdf_template.html')

        context = {
            'personal_info': PersonalInfo.objects.last(),
            'education': Education.objects.last(),
            'experience': Experience.objects.last(),
        }

        html = template.render(context)
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = 'attachment; filename="cv.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=pdf_response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return pdf_response

def cv_form(request):
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST, request.FILES)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)


        personal_info = personal_info_form.save()
        education = education_form.save()
        experience = experience_form.save()

        return render(request, 'cv/cv_preview.html', {
                'personal_info': personal_info,
                'education': education,
                'experience': experience,
        })
      
    else:
        personal_info_form = PersonalInfoForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()

    return render(request, 'cv/cv_form.html', {
        'personal_info_form': personal_info_form,
        'education_form': education_form,
        'experience_form': experience_form,
    })


