from django.db import models
#python3 manage.py makemigrations
# python3 manage.py migrate
#python3 manage.py createsuperuser
# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    total_goals = models.IntegerField(default=False)
    total_assists = models.IntegerField(default=False)
    market_value = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name