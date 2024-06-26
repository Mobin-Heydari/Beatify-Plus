# Generated by Django 5.0.6 on 2024-06-26 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beats', '0012_delete_beatcategorisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'License',
                'verbose_name_plural': 'Licenses',
            },
        ),
        migrations.CreateModel(
            name='BeatLicenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beat_licenses', to='beats.beat')),
                ('licenses', models.ManyToManyField(to='license.license')),
            ],
            options={
                'verbose_name': 'Beat License',
                'verbose_name_plural': 'Beats Licenses',
            },
        ),
        migrations.CreateModel(
            name='LicenseFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='license/files/', verbose_name='license file')),
                ('license_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='license_files', to='license.license')),
            ],
            options={
                'verbose_name': 'License File',
                'verbose_name_plural': 'License Files',
            },
        ),
    ]
