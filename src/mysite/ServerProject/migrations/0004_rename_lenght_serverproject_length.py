# Generated by Django 3.2.2 on 2021-06-04 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServerProject', '0003_serverproject_lenght'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverproject',
            old_name='lenght',
            new_name='length',
        ),
    ]
