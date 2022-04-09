
import uuid
from msilib.schema import Class
from tkinter import CASCADE

from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=15, null=True,blank=True)
    last_name = models.CharField(max_length=20, null=True,blank=True)
    birth_day = models.DateField(auto_now=False, auto_now_add=False)
    MALE = 'M'
    FEMALE = 'F'
    CHOICES_GENDER= (
        (MALE,'MALE'),
        (FEMALE,'FEMALE'),
    )
    gender = models.CharField(choices=CHOICES_GENDER,max_length=1)
    father = models.ForeignKey('Parent',on_delete=models.SET_NULL,null=True,blank=True,related_name='father_name')
    mother = models.ForeignKey('Parent',on_delete=models.SET_NULL,null=True,blank=True,related_name='mother_name')
    lorn_orphan = models.BooleanField()
    birth_place = models.ForeignKey('Adderess',on_delete=models.CASCADE,related_name='birth_place')
    permanent_adderess = models.ForeignKey('Adderess',on_delete=models.CASCADE,related_name='permanent_adderess',blank=False,null=False)
    present_adderess = models.ForeignKey('Adderess',on_delete=models.CASCADE,related_name='present_adderess',blank=True,null=True)
    contact = models.ForeignKey("Contact",on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} {self.birth_day}'
class Parent(models.Model):
    uuid = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.uuid}'
    
class Adderess(models.Model):
    catonment_board = models.BooleanField()
    house_number = models.CharField(max_length=50)
    ward_number = models.CharField(max_length=50)
    city_union = models.CharField(max_length=50)
    district_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.ward_number} {self.city_union} {self.district_number} {self.district_number}'
    

class Contact(models.Model):
    phone = models.CharField( max_length=50,unique=True)
    email = models.EmailField(max_length=254,blank=True,null=True)
    def __str__(self):
        return f'{self.phone} {self.email}'
