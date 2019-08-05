# Generated by Django 2.2.3 on 2019-08-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190805_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='prev_matches',
        ),
        migrations.AddField(
            model_name='match',
            name='prev_matches',
            field=models.ManyToManyField(blank=True, null=True, related_name='_match_prev_matches_+', to='api.Match'),
        ),
    ]
