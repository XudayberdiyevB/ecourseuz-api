# Generated by Django 4.2.1 on 2023-05-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_rename_views_blog_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('street', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=300, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
