# Generated by Django 2.2.3 on 2019-07-04 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190704_1806'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='game',
            table='game',
        ),
        migrations.AlterModelTable(
            name='match',
            table='match',
        ),
        migrations.AlterModelTable(
            name='tournament',
            table='tournament',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
