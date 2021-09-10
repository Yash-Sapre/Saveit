from django.db import models
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return str(self.name)

class Bookmark(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)



