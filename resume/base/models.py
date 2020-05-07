from django.db import models
from datetime import datetime

# Create your models here.
class tweet(models.Model):
	text = models.CharField(max_length=350)
	date_post = models.DateTimeField(default=datetime.now)