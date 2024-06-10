import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

cidades_url = "https://api.ipma.pt/open-data/distrits-islands.json"
tipos_tempo_url = "https://api.ipma.pt/open-data/weather-type-classe.json"

def get_cidades():
    response = requests.get(cidades_url)
    if response.status_code == 200:
        data = response.json()
        cities = [{'id': item['globalIdLocal'], 'name': item['local']} for item in data['data']]
        return cities
    else:
        return []

def get_weather_types():
    response = requests.get(tipos_tempo_url)
    if response.status_code == 200:
        data = response.json()
        weather_types = {item['idWeatherType']: item['descWeatherTypePT'] for item in data['data']}
        return weather_types
    else:
        return {}

def get_previsao_tempo(city_id, days=1):
    previsao_url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json"

    # Fazer as requisições
    forecast_response = requests.get(previsao_url)
    weather_types = get_weather_types()

    # Verificar se as requisições foram bem-sucedidas
    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()

        # Dados da previsão para os próximos dias
        forecast_list = forecast_data['data'][:days]

        # Previsões com descrições e ícones
        weather_forecast = []
        for daily_forecast in forecast_list:
            idWeatherType = daily_forecast['idWeatherType']
            weather_description = weather_types.get(idWeatherType, "Descrição não disponível")
            icon_filename = f"{idWeatherType}.svg"
            icon_url = f"/static/meteo/{icon_filename}"
            daily_data = {
                'city': next((city['name'] for city in get_cidades() if city['id'] == city_id), "Desconhecida"),
                'date': daily_forecast['forecastDate'],
                't_min': daily_forecast['tMin'],
                't_max': daily_forecast['tMax'],
                'description': weather_description,
                'precipitation': daily_forecast.get('precipitaProb', 0),
                'icon_url': icon_url,
            }
            weather_forecast.append(daily_data)

        return weather_forecast
    else:
        return None

@api_view(['GET'])
def lista_cidade(request):
    cities = get_cidades()
    return Response(cities)

@api_view(['GET'])
def tempo_hoje(request, city_id):
    weather_data = get_previsao_tempo(city_id, days=1)
    return Response(weather_data)

@api_view(['GET'])
def tempo_cinco_dias(request, city_id):
    weather_data = get_previsao_tempo(city_id, days=5)
    return Response(weather_data)

def previsao_view(request):
    cities = get_cidades()
    if request.method == 'POST':
        city_id = request.POST.get('city')
        city_name = next((city['name'] for city in cities if city['id'] == int(city_id)), "Desconhecida")
        weather_forecast = get_previsao_tempo(city_id, days=5)
        if weather_forecast:
            context = {
                'cities': cities,
                'selected_city': city_name,
                'weather_forecast': weather_forecast
            }
        else:
            context = {
                'cities': cities,
                'selected_city': city_name,
                'error': 'Não foi possível obter os dados da previsão meteorológica.'
            }
    else:
        context = {
            'cities': cities,
        }
    return render(request, 'meteo/forecast.html', context)

