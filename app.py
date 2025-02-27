from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

API_Key = "3320d5d40928654963b2d8615e3b95e4"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        cidade = request.form['cidade']
        url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={cidade}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'message': 'Cidade não encontrada'}
    return render_template('index.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)