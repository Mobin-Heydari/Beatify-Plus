# Generated by Django 5.0.6 on 2024-06-25 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beats', '0012_delete_beatcategorisation'),
        ('categories', '0001_initial'),
        ('moods', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeatCategorisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Beat_Categorisation', to='beats.beat')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beat_Categorisation_Category', to='categories.category')),
                ('moods', models.ManyToManyField(blank=True, to='moods.mood')),
                ('tags', models.ManyToManyField(blank=True, to='tags.tag')),
            ],
            options={
                'verbose_name': 'Beat Categorisation',
                'verbose_name_plural': 'Beat Categorisations',
                'ordering': ['beat'],
            },
        ),
    ]