# Generated by Django 4.0.3 on 2022-06-17 04:52

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='blog_title', unique=True, verbose_name='Post Address')),
            ],
        ),
    ]