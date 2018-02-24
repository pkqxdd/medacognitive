# Generated by Django 2.0 on 2018-02-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('med_names', models.TextField(verbose_name='Current Medications')),
                ('med_time', models.TextField(verbose_name='Time to take meds')),
                ('med_left', models.TextField(verbose_name='How Much Left')),
            ],
        ),
        migrations.DeleteModel(
            name='Patients',
        ),
    ]