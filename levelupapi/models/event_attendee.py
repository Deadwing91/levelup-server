from django.db import models


class Event_Attendee(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='Event_Relationships')
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='Gamer_Relationships')
    #join tables typically don't need a related_name