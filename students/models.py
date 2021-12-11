from django.db import models


from schoolUsers.models import UserRegistion

STUDENT_CLASS = [
    ('Nusery','nry'),
    ('LKG', 'lkg'),
    ('UKG', 'ukg'),
    ('1st', '1'),
    ('2nd', '2'),
    ('3rd', '3'),
    ('4th', '4'),
    ('5th', '5'),
    ('6th', '6'),
    ('7th', '7'),
    ('8th', '8'),
    ('9th', '9'),
    ('10th', '10'),
    ('11th', '11'),
    ('12th', '12'),
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
    insitution = models.ForeignKey(UserRegistion, on_delete=models.CASCADE)
    student_code = models.IntegerField()
    fName = models.CharField(max_length=50)
    sName = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    fee = models.IntegerField()
    DOB = models.DateField()
    student_present_class = models.CharField(max_length=10, choices=STUDENT_CLASS, default='Nusery')
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=20, default='.')
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


    def __str__(self):
        return str(self.student_code)