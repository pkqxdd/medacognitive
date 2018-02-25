# Generated by Django 2.0 on 2018-02-24 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_meds_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.TextField(verbose_name='Med name')),
                ('med_comment', models.TextField(verbose_name='Comment')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
    ]
