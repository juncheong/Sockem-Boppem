# Generated by Django 2.2.3 on 2019-07-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190717_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='judge_id',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='judges',
        ),
        migrations.AddField(
            model_name='matchuser',
            name='is_judge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournamentuser',
            name='is_judge',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TournamentJudge',
        ),
    ]
