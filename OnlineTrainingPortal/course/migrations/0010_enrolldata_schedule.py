# Generated by Django 4.0.3 on 2022-10-28 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_coursematerial_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolldata',
            name='schedule',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='course.courseschedule'),
        ),
    ]