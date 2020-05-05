from django.db import models

# Create your models here.
class Student(models.Model):
    row_no = models.TextField()
    name = models.TextField(max_length=40)
    student_class = models.TextField()
    department = models.TextField()
    