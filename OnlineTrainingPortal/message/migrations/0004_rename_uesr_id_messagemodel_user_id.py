# Generated by Django 4.0.3 on 2022-10-28 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_alter_messagemodel_uesr_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagemodel',
            old_name='uesr_id',
            new_name='user_id',
        ),
    ]
