import requests, pprint
from flask import Flask, render_template, request

app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=San+Francisco&appid=d26252a76d0ae9c37b097c87d64c1e77"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def show_weather():
    return render_template('weather_form.html')

@app.route('/weather_results', methods=['get', 'post'])
def weather_results_page():
    city = request.args.get('city')

    params = {
        'q': city,
        'APPID': "d26252a76d0ae9c37b097c87d64c1e77"
    }

    res = requests.get(weather_url, params=params)

    if not res.status_code == 200:
        print("404 found")

    results = res.json()
    temp_in_kelvin = results['main']['temp']
    #temp_in_celsius = temp_in_kelvin(temp_in_kelvin)
    city = results['name']

    print(results)
    pp.pprint(response_json)

    return render_template('weather_results.html', results=results, temp_in_celsius=temp_in_celsius)

#weather_url = "http://api.openweathermap.org/data/2.5/weather?q=San+Francisco&appid=d26252a76d0ae9c37b097c87d64c1e77"

response = requests.get(weather_url)
response_json = response.json()
pp.pprint(response_json)

def temp_in_kelvin(k):
    temp_in_celsius = temp_in_kelvin - 273.15
    return int(temp_in_celsius)
    print("it is now " + str(temp_in_celsius) + " degrees Celsius")


main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]
temp_in_celsius = temp_in_kelvin - 273.15
print("it is now " + str(temp_in_celsius) + " degrees Celsius")

if __name__ == '__main__':
    app.run()
