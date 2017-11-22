from urllib import request
import json

class TemperatureManager():
    class Constants:
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=Mexico,MX&APPID={APIKEY}"
        kelvin_temperature = 273.15
    @classmethod
    def get_temperature(cls):
        try:
            with request.urlopen(cls.Constants.base_url) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                variable_aux = json_data["main"]
                temperature = float(variable_aux["temp"]) - cls.Constants.kelvin_temperature

                return temperature
        except Exception as error:
            print('Error')