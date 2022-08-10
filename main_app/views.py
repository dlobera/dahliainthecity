from unicodedata import name
from django.shortcuts import render
from .models import Place
from django.http import HttpResponse

# class Place: 
#   def __init__(self, name):
#     self.name = name

# places = [
#   Place('Austin, TX'),
#   Place('New York, NY'),
#   Place('Boston, MA'),
#   Place('Nashville, TN'),
#   Place('Portland, OR'),
# ]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Dahlia</h1>')

def about(request):
  return render(request, 'about.html')

def places_index(request):
  places = Place.objects.all()
  return render(request, 'places/index.html', { 'places': places })

def home(request):
  return render(request, 'home.html')

def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  return render(request, 'places/detail.html', { 'place': place })