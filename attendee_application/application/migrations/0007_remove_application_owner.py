# Generated by Django 2.1 on 2018-08-10 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20180810_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='owner',
        ),
    ]
