# Generated by Django 4.2.8 on 2024-01-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pasword',
            new_name='password',
        ),
    ]
