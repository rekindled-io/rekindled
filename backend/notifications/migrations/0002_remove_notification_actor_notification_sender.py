# Generated by Django 4.0.3 on 2022-05-27 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='actor',
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='notification_sender', to='notifications.actor'),
            preserve_default=False,
        ),
    ]
