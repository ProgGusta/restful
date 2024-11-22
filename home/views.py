from django.shortcuts import render
from drones.models import Drone

# Create your views here.
def home_page(request):
    drones = Drone.objects.filter(is_published=True)
    return render(request, "home/index.html", {"drones": drones})
