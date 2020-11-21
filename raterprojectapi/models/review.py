from django.db import models
from django.db.models.deletion import CASCADE

class Review(models.Model):
  review = models.CharField(max_length=220)
  rate = models.IntegerField()
  player = models.ForeignKey("Player",
    on_delete=CASCADE,
    related_name="players",
    related_query_name="review"
  )
  game = models.ForeignKey("Game",
    on_delete=CASCADE,
    related_name="games",
    related_query_name="review"
  )
