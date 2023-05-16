# Generated by Django 4.2.1 on 2023-05-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_managers_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTypes',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'supervisor'), (4, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='user_types', to='users.usertypes'),
        ),
    ]