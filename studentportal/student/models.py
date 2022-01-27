from django.db import models, connections
from django.contrib.auth.models import User

class Signup(models.Model):
    username = models.CharField(max_length=100, unique=True)
    pwd = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    cgpa = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "student_signup"


