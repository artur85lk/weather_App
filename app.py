import configparser
import sys
import requests
from flask import Flask, render_template,request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET','POST'])
def add_city():
    if request.method == 'POST':
        user = request.form['city_name']
        city = user
        api_k = "6748a1117fe3e74184446121f31624d6"
        dict_with_weather_info = get_api_weather(city,api_k)
        return render_template('app.html', weather=dict_with_weather_info['city'], weather2=dict_with_weather_info['current temperature'], weather3=dict_with_weather_info['current weather'])

def get_api_weather(city, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    r = requests.get(api_url)
    date = dict(r.json())
    # print(date)
    name = date["name"]
    temp = int(date["main"]["temp"]) - 273
    current_weatcher = date["weather"][0]["main"]
    dict_with_weather_info = {'city': name, 'current temperature': temp, 'current weather': current_weatcher}
    return dict_with_weather_info

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run(host="localhost", port=8000, debug=True)
