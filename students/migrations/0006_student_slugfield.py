# Generated by Django 3.2.9 on 2021-12-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_insitution'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slugfield',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]