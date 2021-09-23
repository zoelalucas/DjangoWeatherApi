from django.shortcuts import render
import requests
from .form import LocationForm 

def getCityDet(api_key,city):
    city_url=f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}'

    city_response= requests.get(city_url)

    return city_response.json()[0]


def getTemp(api_key,loc_key):
    weather_url=f'http://dataservice.accuweather.com/currentconditions/v1/{loc_key}?apikey={api_key}'

    temp_response=requests.get(weather_url)

    return temp_response.json()


def home(request):
    form=LocationForm(request.POST or None)

    if form.is_valid():
        city=form.cleaned_data['location']

        api_key=('API_KEY')
        
        city_data=getCityDet(api_key,city)

        loc_key=city_data['Key']

        city_name=city_data['EnglishName']

        temp_api_res=getTemp(api_key,loc_key)        

        temp_value=temp_api_res[0]['Temperature']['Metric']['Value']

        is_Day=temp_api_res[0]['IsDayTime']

        context={
            'form':form,
            'city_name':city_name,
            'is_Day':is_Day,
            'temperature':temp_value
        }

        return render(request,'weather_app/index.html',context)
    
    return render(request,'weather_app/index.html',context={
        'form':form
    })
