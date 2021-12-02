from django.db import models

STUDENT_CLASS = [
    ('nry', 'Nusery'),
    ('lkg', 'LKG'),
    ('ukg', 'UKG'),
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
    ('5', '5th'),
    ('6', '6th'),
    ('7', '7th'),
    ('8', '8th'),
    ('9', '9th'),
    ('10', '10th'),
    ('11', '11th'),
    ('12', '12th'),
]

RELIGION = [
    ('mus', 'MUSLIM'),
    ('hd', 'HINDU'),
    ('ch', 'CHRISTIAN'),
    ('at', 'ATHEIST'),
    ('sk', 'SIKH'),
]

# Create your models here.
class Student(models.Model):
    student_code = models.IntegerField()
    fName = models.CharField(max_length=50)
    sName = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    fee = models.IntegerField()
    # DOB = models.DateField()
    age = models.IntegerField()
    student_present_class = models.CharField(max_length=5, choices=STUDENT_CLASS, default='Nusery')
    address = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    religion = models.CharField(max_length=10, choices=RELIGION)
    caste = models.CharField(max_length=10)
    last_year_percentage = models.CharField(max_length=3)
    rte_student = models.BooleanField()
    relatives_in_school = models.CharField(max_length=50)



