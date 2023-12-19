from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    trainer = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name