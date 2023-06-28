from django.db import models

# Create your models here.
class Food(models.Model):
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    fats = models.FloatField()
    proteins = models.FloatField()
    calories = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    