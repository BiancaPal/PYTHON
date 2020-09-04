from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'

darksky = DarkSky(API_KEY)

latitude = 60.567402
longitude = -151.246719
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)


print(forecast.currently.temperature)

forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
forecast.alerts # [Alert]. Can be finded at darksky/forecast.py


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Homepage'
    weather = forecast.currently.summary
    return render_template('index.html', title=title, weather=weather)

@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html',title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.html',title=title)
