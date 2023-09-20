import requests

from django.shortcuts import render


def index(request):
    context = {}

    response = requests.get('http://micro_bangkok:8000/')
    data = response.json()
    context['bangkok'] = data['celsius']

    response = requests.get('http://micro_tokyo:3000/')
    data = response.json()
    context['tokyo'] = data['celsius']

    response = requests.get('http://micro_munich:8000/')
    data = response.json()
    context['munich'] = data['celsius']

    response = requests.get('http://micro_nyc:9292/')
    data = response.json()
    context['nyc'] = data['celsius']

    return render(
        request,
        'index.html',
        context
    )
