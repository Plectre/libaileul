
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=32, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return(self.title)