# Generated by Django 4.0.3 on 2022-10-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_coursematerial_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerial',
            name='time',
            field=models.IntegerField(help_text='Duration of the quiz in minutes', null=True),
        ),
    ]
