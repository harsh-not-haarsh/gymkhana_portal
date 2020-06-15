from django.db import models
import datetime


class Team(models.Model):
    TEAM_CHOICES = (
        ('UG', 'UG'),
        ('PG', "PG"),
    )
    YEAR_CHOICES = [(str(x), str(x)) for x in range(int(datetime.datetime.now().year), 2007, -1)]

    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    team_type = models.CharField(max_length=4, choices=TEAM_CHOICES)
    student_heads = models.ManyToManyField("oauth.UserProfile", related_name="heads")
    student_assistant_heads = models.ManyToManyField("oauth.UserProfile", related_name="asstHeads")
    student_guides = models.ManyToManyField("oauth.UserProfile", related_name="sg")

    def __str__(self):
        return self.team_type + self.year
