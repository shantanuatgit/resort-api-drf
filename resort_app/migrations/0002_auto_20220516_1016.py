# Generated by Django 2.2.13 on 2022-05-16 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resort_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
