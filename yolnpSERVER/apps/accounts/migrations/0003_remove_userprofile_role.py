# Generated by Django 4.1.4 on 2022-12-23 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_options"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="role",),
    ]