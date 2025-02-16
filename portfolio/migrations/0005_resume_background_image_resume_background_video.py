# Generated by Django 5.1.6 on 2025-02-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_resume_resskill_language_expertise_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Set Background Image'),
        ),
        migrations.AddField(
            model_name='resume',
            name='background_video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Set Background Video'),
        ),
    ]
