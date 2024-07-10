# Generated by Django 5.0.6 on 2024-07-10 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_user_event_created_by_alter_event_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
        migrations.AddField(
            model_name='event',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
