# Generated by Django 4.2.7 on 2024-01-19 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_pincode_resume_pin_alter_resume_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resume',
        ),
    ]