# Generated by Django 4.2.11 on 2024-09-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_is_suspended'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_googleauth',
            field=models.BooleanField(default=False),
        ),
    ]
