# Generated by Django 4.0.3 on 2022-03-08 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='message',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
    ]
