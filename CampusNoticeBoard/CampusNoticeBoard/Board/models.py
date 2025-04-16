from django.db import models

# Create your models here.
class Student(models.Model):
  Reg_no= models.CharField(max_length=50,primary_key=True)
  Username= models.CharField(max_length=100)
  Name= models.CharField(max_length=255)
  Password= models.CharField(max_length=20)
  Role= models.CharField(max_length=50 , default='student')
  Program=models.CharField(max_length=255)

  def __str__(self):
        return self.Name
  
