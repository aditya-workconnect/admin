from django.db import models

class Institute(models.Model):
    name = models.CharField(max_length=100)

    