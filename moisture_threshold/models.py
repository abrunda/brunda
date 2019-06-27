from django.db import models

# Create your models here.
# Create your models here.
class moisture_threshold(models.Model):
	hardware_id=models.IntegerField(50)
	threshold=models.IntegerField(50)
	