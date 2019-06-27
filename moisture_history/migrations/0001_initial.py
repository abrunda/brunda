# Generated by Django 2.2.2 on 2019-06-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moisture_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_id', models.IntegerField(max_length=50)),
                ('reading_timestamp', models.DateTimeField(auto_now_add=True)),
                ('reading_value', models.IntegerField(verbose_name=50)),
            ],
        ),
    ]
