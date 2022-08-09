from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

class Place: 
  def __init__(self, name):
    self.name = name

places = [
  Place('Austin, TX'),
  Place('New York, NY'),
  Place('Boston, MA'),
  Place('Nashville, TN'),
  Place('Portland, OR'),
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Dahlia</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def places_index(request):
  return render(request, 'places/index.html', { 'places': places })