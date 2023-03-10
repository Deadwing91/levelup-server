from django.db import models


class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE
    , related_name='Events')
    game = models.ForeignKey("Game", on_delete=models.CASCADE
    , related_name='Scheduled_Events')
    name = models.CharField(max_length=150)
    date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=155)
    attendees = models.ManyToManyField("Gamer", through="Event_Attendee", related_name='EventAttendees_gamer')
    #related name will add a related name to the property


    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
        