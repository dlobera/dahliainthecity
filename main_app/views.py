from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Place
from .forms import VisitForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def places_index(request):
  places = Place.objects.filter(user=request.user)
  return render(request, 'places/index.html', { 'places': places })

@login_required
def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  visiting_form = VisitForm()
  return render(request, 'places/detail.html', { 
    'place': place, 'visiting_form': visiting_form
  })

@login_required
def add_visit(request, place_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.place_id = place_id
    new_visit.save()
  return redirect('places_detail', place_id=place_id)

class PlaceCreate(LoginRequiredMixin, CreateView):
  model = Place
  fields = '__all__'
  success_url = '/places/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class PlaceUpdate(LoginRequiredMixin, UpdateView):
  model = Place
  fields = ['todo']

class PlaceDelete(LoginRequiredMixin, DeleteView):
  model = Place
  success_url = '/places/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('places_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)