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
class Event(models.Model):
    Id=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=10000) 
    Category=models.CharField(max_length=100)
    Date=models.DateField()
    
    def __str__(self):
        return self.Title
#class Comments(models.Model):
 #   Comment_id=models.AutoField(primary_key=True)
 #   Id=models.ForeignKey()
    