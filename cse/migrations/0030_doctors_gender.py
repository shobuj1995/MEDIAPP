# Generated by Django 2.2 on 2019-05-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0029_doctors_doctorphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
