# Generated by Django 3.1.7 on 2021-03-29 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_name', models.CharField(max_length=15)),
                ('note_desc', models.CharField(max_length=200)),
                ('note_status', models.BooleanField(verbose_name='note status')),
                ('note_date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
