from django.db import models

# Create your models here.
class Student(models.Model):
  Reg_no= models.AutoField(primary_key=True)
  Username= models.CharField(max_length=100)
  Name= models.CharField(max_length=255)
  Password= models.CharField(max_length=20)
  Role= models.CharField(max_length=50 , default='student')

  def __str__(self):
        return self.Name
    
class Notice(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=10000) 
    category=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
   Comment_id=models.AutoField(primary_key=True)
   Noticeid = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='Comments', null=True)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   Username=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student')
def __str__(self):
    return f'Comment on {self.Notice.title}'

from django.contrib.auth.models import User

class Like(models.Model):
    Likeid= models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='likes', null=True)
    Username= models.ForeignKey(Student, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('Likeid', 'Username')  # prevent duplicate likes

    def __str__(self):
        return f"{self.Student.Username} liked {self.Notice.title}"

    