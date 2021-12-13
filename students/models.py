from django.db import models

from django.urls import reverse


STUDENT_CLASS = [
    ('NUSERY','NUSERY'),
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]

RELIGION = [
    ('MUSLIM', 'MUSLIM'),
    ('HINDU', 'HINDU'),
    ('CHRISTIAN', 'CHRISTIAN'),
    ('ATHEIST', 'ATHEIST'),
    ('SIKH', 'SIKH'),
]


CATEGORY = [
    ('SC', 'SC'),
    ('OBC', 'OBC'),
    ('ST', 'ST'),
    ('GENERAL', 'GENERAL')
]

# Create your models here.
class Student(models.Model):
    insitution = models.CharField(max_length=50)
    student_code = models.IntegerField()
    fName = models.CharField(max_length=50)
    sName = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    fee = models.IntegerField()
    DOB = models.DateField()
    student_present_class = models.CharField(max_length=10, choices=STUDENT_CLASS, default='Nusery')
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=30, default='.')
    city = models.CharField(max_length=50, default='.')
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    adhaar = models.IntegerField(default=12345)
    religion = models.CharField(max_length=10, choices=RELIGION)
    caste = models.CharField(max_length=10)
    category = models.CharField(max_length=10, choices=CATEGORY)
    last_year_percentage = models.CharField(max_length=3, default=0)
    rte_student = models.BooleanField()
    relatives_in_school = models.CharField(max_length=50)
    slugfield = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return str(self.student_code)


    def save(self, *args, **kwargs):
        if self.fName and self.sName and self.student_present_class:
            self.slugfield = str(self.fName).title() + '/' + str(self.sName).title() + '/' + str(self.student_present_class)
        super(Student, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('students:detail', args=[self.id])