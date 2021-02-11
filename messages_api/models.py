from django.db import models


class CreateMessage(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=2893, blank=True)

    def __str__(self):
        return self.message
