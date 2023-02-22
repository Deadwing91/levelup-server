# Generated by Django 4.1.6 on 2023-02-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_game_number_of_players_game_skill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='EventAttendees_gamer', through='levelupapi.Event_Attendee', to='levelupapi.gamer'),
        ),
    ]