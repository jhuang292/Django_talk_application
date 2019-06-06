from django.db import models

class Talk(models.Model):
    talk_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Speaker = models.CharField(max_length=200)
    Venue = models.CharField(max_length=200)
    Duration = models.CharField(max_length=200)

    def __str__(self):
        return self.Name