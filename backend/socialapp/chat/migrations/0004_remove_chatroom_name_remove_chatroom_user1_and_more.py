# Generated by Django 4.2.11 on 2024-10-11 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_chatroom_user1_chatroom_user2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='name',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='room_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='participants',
            field=models.ManyToManyField(related_name='chatrooms', to=settings.AUTH_USER_MODEL),
        ),
    ]