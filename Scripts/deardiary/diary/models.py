from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)

class diaryEntry(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE,related_name="entries")
    name=models.CharField(max_length=30)
    dateTime=models.DateTimeField()
    entry=models.TextField()

    class Meta():
        ordering=["-dateTime"]
