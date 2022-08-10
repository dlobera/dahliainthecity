from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

# Create your models here.
class Place(models.Model):
  name = models.CharField(max_length=100)
  todo = ArrayField(
      ArrayField(
            models.CharField(max_length=10, blank=True),
            size=20,
        ),
        size=20,
    )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('places_detail', kwargs={'place_id': self.id})

# Add new Feeding model below Cat model
class Visit(models.Model):
  date = models.DateField()
  meal = models.CharField(max_length=1)