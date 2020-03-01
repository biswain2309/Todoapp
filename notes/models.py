from django.db import models

class Notes(models.Model):
    description = models.CharField(max_length=20)
