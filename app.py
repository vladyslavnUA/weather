import requests, pprint
from flask import Flask, render_template, request

app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
weather_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def show_weather():
    return render_template('weather_form.html')

@app.route('/weather_results', methods=['get', 'post'])
def weather_results_page():
    user_city = request.args.get('city')
    params = {
        'q': user_city,
        'appid': '2608f679d4594364525f6c6cc2246c79'
    }

    res = requests.get(weather_url, params=params)
    if not res.status_code == 200:
        print("404 found")
    results = res.json()
    city = results['name']

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=San+Francisco&appid=2608f679d4594364525f6c6cc2246c79"

response = requests.get(weather_url)
response_json = response.json()
pp.pprint(response_json)

main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]
temp_in_celsius = temp_in_kelvin - 273.15
print("it is now " + str(temp_in_celsius) + " degrees Celsius")