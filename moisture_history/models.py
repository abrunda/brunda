from django.db import models

# Create your models here.
class moisture_history(models.Model):
	hardware_id=models.IntegerField(max_length=50)
	reading_timestamp=models.DateTimeField(auto_now_add=True)
	reading_value=models.IntegerField(50)