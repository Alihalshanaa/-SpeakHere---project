# Generated by Django 4.1.4 on 2023-01-30 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SpeakHere_app', '0015_threadmodel_messagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='threadnot', to='SpeakHere_app.threadmodel'),
            preserve_default=False,
        ),
    ]
