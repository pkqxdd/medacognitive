# Generated by Django 2.0 on 2018-02-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20180224_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='meds_taken',
            field=models.TextField(null=True, verbose_name='Meds Taken'),
        ),
    ]
