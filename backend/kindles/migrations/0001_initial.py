# Generated by Django 4.0.3 on 2022-03-27 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('handles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekingKindle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=512)),
                ('target_handle', models.CharField(max_length=64)),
                ('subscribe', models.BooleanField(default=True)),
                ('game_and_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.gameandplatform')),
                ('source_handle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='handles.handle')),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DirectKindle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=512)),
                ('source_handle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='handles.handle')),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('target_handle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handles.handle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='seekingkindle',
            constraint=models.UniqueConstraint(fields=('source_user', 'source_handle', 'target_handle'), name='seekingkindle_unique_kindle'),
        ),
        migrations.AddConstraint(
            model_name='directkindle',
            constraint=models.UniqueConstraint(fields=('source_user', 'source_handle', 'target_handle'), name='directkindle_unique_kindle'),
        ),
    ]
