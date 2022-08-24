
from time import timezone
from django.db import models


class LogBook(models.Model):

    user = models.CharField(max_length=20, default="noname")
    date = models.CharField(max_length=20)
    aircraft = models.CharField(max_length=20)
    ident = models.CharField(max_length=20)
    from_airport = models.CharField(max_length=20)
    to_airport = models.CharField(max_length=20)
    start = models.CharField(max_length=20)
    stop = models.CharField(max_length=20)
    flyTime = models.CharField(max_length=20)
    duo = models.BooleanField(default=False, blank=True)
    observations = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user
