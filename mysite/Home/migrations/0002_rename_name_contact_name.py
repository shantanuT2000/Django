# Generated by Django 4.0.5 on 2022-06-20 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
    ]
