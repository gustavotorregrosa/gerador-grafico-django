from django.http import HttpResponse, request
from django.shortcuts import render
from .services.service_clientes import ServiceClientes
from django.http import JsonResponse
import json
from gerador_grafico.utils import transform_list_to_json

# Create your views here.
def listar_clientes(request):
    clients = ServiceClientes().listar_clientes()
    clientsJSON = transform_list_to_json(clients)
    return JsonResponse(clientsJSON, safe=False)



