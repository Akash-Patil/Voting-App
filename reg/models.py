from django.db import models
from django import forms

# Create your models here.

class Member(models.Model):
    Name=models.CharField(max_length=40)
    #Regions=models.TextChoices('Region', 'North South East West')
    #Region= models.CharField(blank=True, choices=Regions.choices, max_length=10)
    Email=models.CharField(max_length=30, primary_key=True)
    Password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.Name + " / " + self.Email #display on admins website
   
  
    class Meta:  
        db_table = "web_member"  # name of db
