from django.db import models
from django.urls import reverse

# Create your models here.

RESULTS = (
    ('W', 'Win'),
    ('L', 'Lose')
)

class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    trainer = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Battle(models.Model):
    date = models.DateField('Battle Date')
    enemy = models.CharField(max_length=25)
    result = models.CharField(
        max_length=1,
        choices=RESULTS
    )

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_result_display()} vs {self.enemy} on {self.date}"

    class Meta:
        ordering = ['date']