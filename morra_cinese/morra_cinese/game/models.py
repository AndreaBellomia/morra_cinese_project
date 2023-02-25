from django.db import models


class Game(models.Model):
    """ Models For save a games """

    user_name = models.CharField(max_length=80)
    match_win = models.IntegerField(default=0)
    match_tie = models.IntegerField(default=0)
    match_lost = models.IntegerField(default=0)

    game_date = models.DateTimeField(auto_now_add=True)

    closed_game = models.BooleanField(default=False)