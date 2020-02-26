from django.db import models

class Notes(models.Model):
    description = models.TextField()
