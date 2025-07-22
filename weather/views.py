from django.shortcuts import render,redirect
import requests


def home(request):
    weather_data = None
    if request.method == 'POST':
        api_key = 'aaf4784cd77f23bd577a4217086a9e4f'
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
                    
            data = response.json()
            weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description':data['weather'][0]['description'],
            'weather_icon': data['weather'][0]['icon'],
            'wind_speed':data['wind']['speed'],
            'humidity':data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'country_code' : data['sys']['country'],
            }
        else:
            return redirect('home')

    return render(request, 'home.html',{'weather':weather_data})
# Create your views here.
