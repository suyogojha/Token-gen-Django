# Generated by Django 4.0.3 on 2022-03-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_email_student_age_remove_student_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.TextField(blank=True, null=True),
        ),
    ]
