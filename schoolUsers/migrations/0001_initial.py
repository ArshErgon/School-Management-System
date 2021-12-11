# Generated by Django 3.2.9 on 2021-12-04 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=10)),
                ('Sname', models.CharField(max_length=10)),
                ('insitution', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('adhaar', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('studentCode', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
