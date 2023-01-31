from django.db import models

# Create your models here.

class Remind(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    time = models.DateTimeField()
    description = models.TextField(max_length=10000, default=' ')

    def __str__(self):
        return self.name