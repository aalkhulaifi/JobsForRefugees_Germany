# Generated by Django 2.0.4 on 2018-05-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_task_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_request',
            name='status',
            field=models.NullBooleanField(),
        ),
    ]
