from django.db import models

# Create your models here.


class TeacherModel(models.Model):
    insitution  = ""
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.fName