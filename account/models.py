from tabnanny import verbose
from django.db import models
from logbook.models import LogBook

class Users(models.Model):

    callSign = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    logBook = models.ForeignKey(LogBook,blank=True ,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.callSign

