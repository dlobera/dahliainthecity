from django.contrib.postgres.fields import ArrayField
from django.db import models

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