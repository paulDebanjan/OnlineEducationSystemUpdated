# Generated by Django 4.0.3 on 2022-10-28 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0002_messagemodel_uesr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='uesr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]