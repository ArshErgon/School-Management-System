from django.db import models

# Create your models here.
class UserRegistion(models.Model):
    Fname = models.CharField(max_length=10)
    Sname = models.CharField(max_length=10)
    insitution = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phone_number = models.IntegerField()
    adhaar = models.IntegerField()
    username = models.CharField(max_length=50)
    email = models.EmailField()
    studentCode = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Fname[:5] + self.insitution


