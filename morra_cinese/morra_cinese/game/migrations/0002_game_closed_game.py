# Generated by Django 4.1.7 on 2023-02-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='closed_game',
            field=models.BooleanField(default=False),
        ),
    ]
