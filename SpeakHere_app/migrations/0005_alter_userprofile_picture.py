# Generated by Django 4.1.4 on 2023-01-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpeakHere_app', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures'),
        ),
    ]
