# Generated by Django 3.0.3 on 2020-02-15 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brieflist',
            name='status',
            field=models.CharField(choices=[('P', 'Public'), ('R', 'Private')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='status',
            field=models.CharField(choices=[('P', 'Public'), ('R', 'Private')], default='P', max_length=1),
        ),
    ]
