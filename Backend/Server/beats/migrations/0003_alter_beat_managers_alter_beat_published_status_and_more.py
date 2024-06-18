# Generated by Django 5.0.6 on 2024-06-16 12:57

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0002_alter_beat_published_status_alter_beat_status_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='beat',
            managers=[
                ('accepted', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='beat',
            name='published_status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Private', 'Private'), ('Published', 'Published')], default='Draft', max_length=9, verbose_name='published status'),
        ),
        migrations.AlterField(
            model_name='beat',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Checking', 'Checking'), ('Rejected', 'Rejected')], default='Checking', max_length=8),
        ),
    ]