from django.db import models

# Create your models here.
class todoItem(models.Model):
    item_text=models.CharField(max_length=200)
    added_date=models.DateTimeField()
