# Generated by Django 4.1.6 on 2023-02-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_alter_game_gametype'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.CharField(default='Easy', max_length=12),
        ),
    ]
