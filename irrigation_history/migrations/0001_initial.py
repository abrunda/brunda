# Generated by Django 2.2.2 on 2019-06-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='irrigation_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_id', models.IntegerField(max_length=50)),
                ('irrigation_timestamp', models.DateField(verbose_name=50)),
                ('temperature', models.FloatField(verbose_name=50)),
                ('before_moisture', models.IntegerField(verbose_name=50)),
                ('after_moisture', models.IntegerField(verbose_name=50)),
            ],
        ),
    ]
