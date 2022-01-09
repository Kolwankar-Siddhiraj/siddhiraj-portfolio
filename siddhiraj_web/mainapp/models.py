from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.

class my_profile(models.Model):
    status = models.IntegerField(default=1, null=True)
    my_full_name = models.CharField(max_length=100, blank=True, null=True)
    my_first_name = models.CharField(max_length=50, blank=True, null=True)
    my_middle_name = models.CharField(max_length=50, blank=True, null=True)
    my_last_name = models.CharField(max_length=50, blank=True, null=True)
    my_job_post = models.CharField(max_length=100, blank=True, null=True)
    my_about_me = models.TextField(max_length=5000, blank=True, null=True)
    my_email = models.EmailField(max_length=50, blank=True, null=True)
    my_email_display = models.BooleanField(default=False)
    my_email_alt = models.EmailField(max_length=50, blank=True, null=True)
    my_gender = models.CharField(max_length=25, blank=True, null=True)
    my_address = models.TextField(max_length=2000, blank=True, null=True)
    my_age = models.CharField(max_length=20, blank=True, null=True)
    my_profile_pic = models.ImageField(upload_to="admin_images")
    my_phone = models.IntegerField()
    my_phone_display = models.BooleanField(default=False)
    my_resume = models.FileField(upload_to="admin_files_resume")

    def __str__(self):
        return self.my_profile_status




class my_education(models.Model):
    status = models.IntegerField(default=1, null=True)
    edu_name = models.CharField(max_length=500, blank=True,null=True)
    edu_institute_name = models.CharField(max_length=500, blank=True,null=True)
    edu_date = models.CharField(max_length=100, blank=True,null=True)
    edu_description = models.TextField(max_length=3000, blank=True,null=True)
    edu_additional_info = models.TextField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.edu_name


class my_experience(models.Model):
    status = models.IntegerField(default=1, null=True)
    exp_name = models.CharField(max_length=500, blank=True,null=True)
    exp_org_name = models.CharField(max_length=500, blank=True,null=True)
    exp_date = models.CharField(max_length=100, blank=True,null=True)
    exp_description = models.TextField(max_length=3000, blank=True,null=True)
    exp_additional_info = models.TextField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.exp_name




class my_certification(models.Model):
    status = models.IntegerField(default=1, null=True)
    cer_name = models.CharField(max_length=500, blank=True,null=True)
    cer_org_name = models.CharField(max_length=500, blank=True,null=True)
    cer_date = models.CharField(max_length=500, blank=True,null=True)
    cer_description = models.TextField(max_length=2000,blank=True,null=True)
    cer_file = models.FileField(upload_to="certificate_files")
    cer_url = models.URLField(max_length=500)
    cer_tags = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.cer_name



class blog(models.Model):
    status = models.IntegerField(default=1, null=True)
    blog_title = models.CharField(max_length=500, blank=True,null=True)
    blog_image = models.ImageField(upload_to="blog_images")
    blog_description = models.CharField(max_length=500, blank=True,null=True)
    blog_date = models.CharField(max_length=500, blank=True,null=True)
    blog_subject = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.blog_title


class my_code_skills(models.Model):
    status = models.IntegerField(default=1, null=True)
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.IntegerField()

    def __str__(self):
        return self.skill_name



class my_other_skills(models.Model):
    status = models.IntegerField(default=1, null=True)
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.IntegerField()

    def __str__(self):
        return self.skill_name




class projects(models.Model):
    status = models.IntegerField(default=1, null=True)
    project_title = models.CharField(max_length=500, blank=True,null=True)
    project_image = models.ImageField(upload_to="project_images")
    project_description = models.CharField(max_length=500, blank=True,null=True)
    project_date = models.CharField(max_length=500, blank=True,null=True)
    project_url_live = models.URLField(max_length=500)
    project_url_code = models.URLField(max_length=500)

    def __str__(self):
        return self.project_title



class skill_area(models.Model):
    status = models.IntegerField(default=1, null=True)
    sa_name = CharField(max_length=100)
    sa_description = CharField(max_length=100)
    sa_image = ImageField(upload_to="skill_area_images")

    def __str__(self):
        return self.sa_name



class stats(models.Model):
    profile_visits = models.IntegerField()


