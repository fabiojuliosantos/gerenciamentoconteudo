# Generated by Django 4.2.2 on 2023-06-29 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categories',
        ),
    ]
