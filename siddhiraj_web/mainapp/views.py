# from django.shortcuts import render

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import *



# Create your views here.

all_models = [my_profile, my_education, my_experience, my_certification, my_code_skills, my_other_skills, blog, projects, skill_area, stats ]

# All views STARTS here

def index(request):

    profile = my_profile.objects.filter(status=1)
    edu = my_education.objects.filter(status=1)
    exp = my_experience.objects.filter(status=1)
    cer = my_certification.objects.filter(status=1)
    code_skill = my_code_skills.objects.filter(status=1)
    other_skill = my_other_skills.objects.filter(status=1)
    blg = blog.objects.filter(status=1)
    prj = projects.objects.filter(status=1)
    skill_a = skill_area.objects.filter(status=1)
    sts = stats.objects.get()


    return render(request, "index.html", {"profile":profile, "edu":edu, "exp":exp, "cer":cer, "code_skill":code_skill, "other_skill":other_skill, "blg":blg, "prj":prj, "skill_a":skill_a, "sts":sts})

def index1(request):
    return render(request, "index-2.html")



# All views ENDS here


