# Generated by Django 4.2.1 on 2023-05-16 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='views',
            new_name='views_count',
        ),
    ]
