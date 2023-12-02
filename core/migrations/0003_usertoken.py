# Generated by Django 4.2.7 on 2023-12-02 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_sensordetail_options_sensor_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]