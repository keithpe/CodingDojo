# Generated by Django 2.2 on 2020-06-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200615_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]