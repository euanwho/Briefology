# Generated by Django 3.0.3 on 2020-06-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictation',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
            preserve_default=False,
        ),
    ]