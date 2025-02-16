# Generated by Django 5.1.6 on 2025-02-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_contactinfo_addres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero_page',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='hero_page',
            name='background_video',
        ),
        migrations.AddField(
            model_name='hero_page',
            name='background_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='image', max_length=10),
        ),
        migrations.AddField(
            model_name='hero_page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hero_page',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
