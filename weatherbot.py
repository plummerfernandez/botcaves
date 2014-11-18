#A bot to check the weather using the python weather API
# https://code.google.com/p/python-weather-api/

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.get_weather_from_yahoo('RSXX0199', 'metric')
pp.pprint(result)

temperature = weather_com_result['current_conditions']['temperature']
