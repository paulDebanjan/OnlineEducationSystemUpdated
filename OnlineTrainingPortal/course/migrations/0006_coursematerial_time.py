# Generated by Django 4.0.3 on 2022-10-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_coursematerial_number_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerial',
            name='time',
            field=models.IntegerField(default=0, help_text='Duration of the quiz in minutes'),
        ),
    ]