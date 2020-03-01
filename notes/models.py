from django.db import models

class Notes(models.Model):
    description = models.CharField(max_length=20)

    class Meta:
        db_table = "Notess"
