from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

VISITED = (
  ('1', 'Visited'),
  ('2', 'Not Visited'),
)

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
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('places_detail', kwargs={'place_id': self.id})

class Visit(models.Model):
  date = models.DateField()
  visited = models.CharField(
    max_length=1,
    choices=VISITED,
    default=VISITED[0][0]
  )
  place = models.ForeignKey(Place, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_visited_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

