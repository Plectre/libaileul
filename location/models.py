from datetime import timezone
from django.db import models
from django.utils import timezone

class Location(models.Model):
    nom = models.CharField(max_length=50, blank=False)
    prenom = models.CharField(max_length=50, blank=False, default="")
    machine = models.CharField(max_length=50, blank=False)
    start = models.DateTimeField(default=timezone.now, blank=False)
    end = models.DateTimeField(default=timezone.now, blank=False)


    def __str__(self):
        return self.nom
