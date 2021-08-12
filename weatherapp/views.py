from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid=83b7dd61a0d17cecd354e1b94a36d980'
        city = request.POST['city']

        r = requests.get(url.format(city)).json()
   

        city_weather = {
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        print(city_weather)
        return render(request,'index.html',{'cast':city_weather})
    else:
        return render(request,'index.html')
    
   
