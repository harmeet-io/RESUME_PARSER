# Generated by Django 3.2.12 on 2023-02-07 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeBuilder', '0003_rename_user_resume_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='user_id',
            new_name='user',
        ),
    ]