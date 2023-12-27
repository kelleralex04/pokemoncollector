from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

# Create your models here.

RESULTS = (
    ('W', 'Win'),
    ('L', 'Lose')
)

TYPES = (
    ('A', 'Normal'),
    ('B', 'Fire'),
    ('C', 'Water'),
    ('D', 'Electric'),
    ('E', 'Grass'),
    ('F', 'Ice'),
    ('G', 'Fighting'),
    ('H', 'Poison'),
    ('I', 'Ground'),
    ('J', 'Flying'),
    ('K', 'Psychic'),
    ('L', 'Bug'),
    ('M', 'Rock'),
    ('N', 'Ghost'),
    ('O', 'Dragon'),
    ('P', 'Dark'),
    ('Q', 'Steel'),
    ('R', 'Fairy')
)

CATEGORIES = (
    ('P', 'Physical'),
    ('S', 'Special'),
    ('T', 'Status')
)

class Move(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )
    power = models.IntegerField()
    accuracy = models.IntegerField(
        validators=[MaxValueValidator(100)]
    )
    pp = models.IntegerField()
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('moves_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    trainer = models.CharField(max_length=25)
    moves = models.ManyToManyField(Move)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Battle(models.Model):
    date = models.DateField('Battle Date')
    enemy = models.CharField(max_length=25)
    result = models.CharField(
        max_length=1,
        choices=RESULTS,
        default=RESULTS[0][0]
    )

    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_result_display()} vs {self.enemy} on {self.date}"

    class Meta:
        ordering = ['date']