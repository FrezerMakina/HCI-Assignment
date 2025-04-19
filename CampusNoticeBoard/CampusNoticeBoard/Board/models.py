from django.db import models

# Create your models here.
class Student(models.Model):
  Reg_no= models.CharField(max_length=50,primary_key=True)
  Username= models.CharField(max_length=100)
  Email= models.CharField(max_length=100, default='student@mubas.ac.mw')
  Name= models.CharField(max_length=255)
  Password= models.CharField(max_length=20)
  Role= models.CharField(max_length=50 , default='student')
  Program=models.CharField(max_length=255)

  def __str__(self):
        return self.Name
    
class Event(models.Model):
    EventId=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=10000) 
    Category=models.CharField(max_length=100)
    Date=models.DateField()
    
    def __str__(self):
        return self.Title
    
class Comments(models.Model):
   Comment_id=models.AutoField(primary_key=True)
   EventId = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Comments')
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   Username=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student')
def __str__(self):
    return f'Comment on {self.event.Title}'

from django.contrib.auth.models import User

class Like(models.Model):
    EventId= models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    Username= models.ForeignKey(Student, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('EventId', 'Username')  # prevent duplicate likes

    def __str__(self):
        return f"{self.Student.Username} liked {self.event.Title}"

    