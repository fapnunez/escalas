# Generated by Django 3.2.5 on 2021-07-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20210710_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escala',
            name='disponivel',
        ),
    ]