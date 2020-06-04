# Generated by Django 3.0.3 on 2020-06-03 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dictations', '0003_dictation_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictation',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='dictation',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
