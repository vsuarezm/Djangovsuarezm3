from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def measure(request):
    if 'cedula' and 'nombre' and 'actividad' and 'estrato' in request.GET:
        cedula = request.GET['cedula']
        nombre = request.GET['nombre']
        actividad = request.GET['actividad']
        estrato = request.GET['estrato']
    # Verifica si hay un parámetro value en la petición GET
        if cedula:
            # Crea el json para realizar la petición POST al Web Service
            args = {'cedula':cedula, 'nombre': nombre,'actividad':actividad,'estrato':estrato}
            response = requests.post('http://127.0.0.1:8000/measures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})
