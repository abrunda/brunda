# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class login_data(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)


class user_hardware_mapping(models.Model):
	user_name=models.CharField(max_length=100)
	hardware_id = models.IntegerField(max_length=50)
	hardware_reference_name = models.CharField(max_length=100)
	crop_name=models.CharField(max_length=100)

class soil_moisture_dictonary(models.Model):
	crop_name=models.CharField(max_length=100)
	wet=models.IntegerField(50)
	normal=models.IntegerField(50)
	dry=models.IntegerField(50)



class irrigation_history(models.Model):
	hardware_id=models.IntegerField(max_length=50)
	irrigation_timestamp=models.DateField(50)
	temperature=models.FloatField(50)
	before_moisture=models.IntegerField(50)
	after_moisture=models.IntegerField(50)

class moisture_history(models.Model):
	hardware_id=models.IntegerField(max_length=50)
	reading_timestamp=models.IntegerField(50)
	reading_value=models.IntegerField(50)


		
class Meta:
        managed = False
        db_table = 'login_data'



		