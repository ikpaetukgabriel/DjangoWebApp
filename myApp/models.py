from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    student_class = models.CharField(max_length=30)
    unique_number = models.IntegerField()