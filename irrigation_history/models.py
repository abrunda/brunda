from django.db import models

# Create your models here.
class irrigation_history(models.Model):
	hardware_id=models.IntegerField(max_length=50)
	irrigation_timestamp=models.DateField(50)
	temperature=models.FloatField(50)
	before_moisture=models.IntegerField(50)
	after_moisture=models.IntegerField(50)