# Generated by Django 3.2.5 on 2021-07-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210716_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=30)),
                ('disponivel', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('nome', 'rua', 'numero')},
            },
        ),
    ]