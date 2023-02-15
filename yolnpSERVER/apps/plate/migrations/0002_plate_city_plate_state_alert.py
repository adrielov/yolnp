# Generated by Django 4.1.6 on 2023-02-13 22:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0006_delete_alert'),
        ('plate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plate',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('plate', models.CharField(max_length=10)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alert', to='camera.camera')),
            ],
        ),
    ]