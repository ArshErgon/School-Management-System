from django.db import models

from django.contrib.auth.models import User

ROLE_NAME = [
    ('PRINCIPAL', 'PRINCIPAL'),
    ('MANAGER', 'MANAGER'),
]


# Create your models here.
class UserRegistion(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Fname = models.CharField(max_length=10)
    Sname = models.CharField(max_length=10)
    insitution = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    adhaar = models.IntegerField()
    role = models.CharField(max_length=10, choices=ROLE_NAME, default='MANAGER')
    schoolCode = models.IntegerField()
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.insitution

    def save(self, *args, **kwargs):
        if self.Fname:
            self.username = self.Fname
        super().save(*args, **kwargs)

        


