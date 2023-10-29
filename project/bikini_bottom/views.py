from django.shortcuts import render
from django.core.serializers import serialize
from .models import Facility
from django.http import HttpResponse, JsonResponse
import ast

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def home_map_api(request):
    data = serialize('geojson', Facility.objects.all())
    return HttpResponse(data, content_type='json')

def custom_map_api(request):
    features = {
        'type': 'FeatureCollection',
        'crs': {
            'type': 'name',
            'properties': {
                'name': 'EPSG:4326'
            }
        },
        'features': []
    }

    model = Facility.objects.all()
    for item in model:
        feature = {
            'type': 'Feature',
            'geometry': ast.literal_eval(item.location.json),
            'properties': {
            'name': item.name,
            'types': item.types,
            'price': item.price,
            'price_unit': item.price_unit
            }
        }
        features['features'].append(feature)
    print(features)

    data = {
        'nama': 'Asep',
        'usia': 23,
        'perempuan': False
    }
    return JsonResponse(features, safe=False)