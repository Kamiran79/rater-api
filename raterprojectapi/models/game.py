#from raterprojectapi.models.categories import Categories
from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
  title = models.CharField(max_length=75)
  designer = models.CharField(max_length=50)
  year_released = models.DateTimeField()
  number_of_players = models.IntegerField()
  estimate_time_to_play = models.DateTimeField()
  age_recommendation = models.IntegerField()
  imgUrl = models.CharField(max_length=255)
  creater = models.ForeignKey("Player",
    on_delete=CASCADE,
    related_name="player",
    related_query_name="game"
  )
  categories = models.ManyToManyField(
    "Category",
    related_name="game_categories",
    related_query_name="game_category"
  )
