from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserSettings(models.Model):
	user = models.ForeignKey(User)
	animals = models.BooleanField(default=False)
	kids = models.BooleanField(default=False)
	fails = models.BooleanField(default=False)
	stereotypes = models.BooleanField(default=False)
	language = models.BooleanField(default=False)
	absurd = models.BooleanField(default=False)

