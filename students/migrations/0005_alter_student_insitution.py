# Generated by Django 3.2.9 on 2021-12-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20211210_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='insitution',
            field=models.TextField(max_length=50),
        ),
    ]
