# Generated by Django 4.2.4 on 2023-08-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]