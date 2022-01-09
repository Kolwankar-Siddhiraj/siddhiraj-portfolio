from django.contrib import admin
from .models import *
# Register your models here.

all_models = [my_profile, my_education, my_experience, my_certification, my_code_skills, my_other_skills, blog, projects, skill_area, stats ]

admin.site.register(all_models)


