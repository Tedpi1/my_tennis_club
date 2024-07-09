from django.db import models
from django.contrib import admin
class Member(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone=models.IntegerField(null=True) 
    joined_date=models.DateField(null=True)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Member, MemberAdmin)

# Create your models here