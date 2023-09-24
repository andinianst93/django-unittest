from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Airport, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        try:
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))
    
# def book(request, flight_id):
#     if request.method == "POST":
#         # Accessing the flight
#         flight = Flight.objects.get(pk=flight_id)

#         # Finding the passenger id from the submitted form data
#         passenger_id = int(request.POST["passenger"])

#         # Finding the passenger based on the id
#         passenger = Passenger.objects.get(pk=passenger_id)

#         # Add passenger to the flight
#         passenger.flights.add(flight)

#         # Redirect user to flight page
#         return HttpResponseRedirect(reverse("flight", args=(flight.id,)))