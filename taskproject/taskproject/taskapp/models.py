from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)