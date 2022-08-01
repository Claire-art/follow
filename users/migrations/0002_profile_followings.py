# Generated by Django 4.0.4 on 2022-08-01 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to='users.profile'),
        ),
    ]