# Generated by Django 4.2.1 on 2023-05-16 14:59

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('desc', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('level', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_picture/')),
                ('video', models.FileField(upload_to='course_video/')),
                ('created_add', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
