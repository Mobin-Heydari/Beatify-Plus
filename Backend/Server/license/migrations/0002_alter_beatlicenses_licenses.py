# Generated by Django 5.0.6 on 2024-06-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beatlicenses',
            name='licenses',
            field=models.ManyToManyField(blank=True, to='license.license'),
        ),
    ]
