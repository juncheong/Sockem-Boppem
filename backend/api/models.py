"""Models for REST API"""
from django.db import models


class User(models.Model):
    """User model. Users can also be judges"""
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=None)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    avatar = models.CharField(max_length=None, null=True)


class Tournament(models.Model):
    """Tournament model"""
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=True)
    start_date = models.DateTimeField(null=True)
    creator_id = models.ForeignKey(User, models.PROTECT)
    users = models.ManyToManyField(User, through='TournamentUser')
    judges = models.ManyToManyField(User, through='TournamentJudge')


class TournamentUser(models.Model):
    """Intermediate table for many-to-many relationship between Tournament and User"""
    tournament_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)


class TournamentJudge(models.Model):
    """Intermediate table for many-to-many relationship between Tournament and User(judge)"""
    tournament_judge_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.PROTECT)


class Match(models.Model):
    """Match model. Round == the round in the tournament. Num_games == # games per match"""
    match_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey(Tournament, models.PROTECT)
    judge_id = models.ForeignKey(User, models.PROTECT)
    round = models.SmallIntegerField()
    num_games = models.SmallIntegerField()
    users = models.ManyToManyField(User, through='MatchUser')


class MatchUser(models.Model):
    """Intermediate table for many-to-many relationship between Match and User"""
    match_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    match_id = models.ForeignKey(Match, on_delete=models.PROTECT)


class Game(models.Model):
    """Game model"""
    game_id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey(Match, models.PROTECT)
    winner_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
