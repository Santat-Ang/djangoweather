from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        LatitudeValue = request.POST['LatitudeValue']
        LongtitudeValue = request.POST['LongtitudeValue']
        api_request = requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat=" + LatitudeValue + "&lon=" + LongtitudeValue + "&appid=b55110fe3f0a0180ad333ebf5ee5aab1")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api['list'][0]['main']['aqi'] == 1 :
            category_description = "Good"
            category_color = "Good"
        elif api['list'][0]['main']['aqi'] == 2 :
            category_description = "Fair"
            category_color = "Fair"
        elif api['list'][0]['main']['aqi'] == 3 :
            category_description = "Moderate"
            category_color = "Moderate"
        elif api['list'][0]['main']['aqi'] == 4 :
            category_description = "Poor"
            category_color = "Poor"
        elif api['list'][0]['main']['aqi'] == 5 :
            category_description = "Very Poor"
            category_color = "VeryPoor"
        else:
            category_description = "Error"
            category_color = "Error"
            
        return render(request,'home.html',{
            'api':api,
            'category_description':category_description,
            'category_color':category_color,
            'LatitudeValue':LatitudeValue,
            'LongtitudeValue':LongtitudeValue
            })
    else:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat=31.5204&lon=74.3587&appid=b55110fe3f0a0180ad333ebf5ee5aab1")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api['list'][0]['main']['aqi'] == 1 :
            category_description = "Good"
            category_color = "Good"
        elif api['list'][0]['main']['aqi'] == 2 :
            category_description = "Fair"
            category_color = "Fair"
        elif api['list'][0]['main']['aqi'] == 3 :
            category_description = "Moderate"
            category_color = "Moderate"
        elif api['list'][0]['main']['aqi'] == 4 :
            category_description = "Poor"
            category_color = "Poor"
        elif api['list'][0]['main']['aqi'] == 5 :
            category_description = "Very Poor"
            category_color = "VeryPoor"
        else:
            category_description = "Error"
            category_color = "Error"

        return render(request,'home.html',{
            'api':api,
            'category_description':category_description,
            'category_color':category_color
            })

def about(request):
    return render(request,'about.html',{})