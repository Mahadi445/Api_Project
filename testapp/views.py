import datetime
from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    try:
        if 'city' in request.POST:
            city = request.POST['city']
    except Exception as e:
        city = 'dhaka'

        
    appid = '3338c1e746b2fe4c762d0d8d265488bc'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    
    PARAMS = {'q': city  ,'appid': appid, 'units' : 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    x = r.json()
    
    context={
            'desc'       : x['weather'][0]['description'],  
            'icon'       : x['weather'][0]['icon'],
            'temp'       : x['main']['temp'],
            'dated'      : datetime.date.today(),  
            'city'       : city,
            'hum'        : x['main']['humidity'], 
            'press'      : x['main']['pressure'],
            'c_code'     : x['sys']['country'],   
            'wind'       : x['wind']['speed'],
            'visibility' :x['visibility'],
 
    }  
    return render(request, 'testapp/index.html',context)





