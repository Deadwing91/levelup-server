from django.db import models


class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE,
    related_name='Created_Games')
    gametype = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='Games')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    designer = models.CharField(max_length=150)

    
