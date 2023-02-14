# Generated by Django 4.1.6 on 2023-02-13 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Game_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('designer', models.CharField(max_length=150)),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Created_Games', to='levelupapi.gamer')),
                ('gametype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Games', to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gamer_Relationships', to='levelupapi.event')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Event_Relationships', to='levelupapi.gamer')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scheduled_Events', to='levelupapi.game'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Events', to='levelupapi.gamer'),
        ),
    ]