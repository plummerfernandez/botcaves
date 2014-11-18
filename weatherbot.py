# a basic weather-checking bot example for the Botcaves workshop

import pywapi
import pprint
import string
from threading import Event, Thread, Timer

pp = pprint.PrettyPrinter(indent=4)


# method for checking the weather
def checkWeather():
	weather_com_result = pywapi.get_weather_from_weather_com('10001')
	#pp.pprint(weather_com_result)
	temperature = weather_com_result['current_conditions']['temperature']
	print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n"


## METHOD TO RUN AT INTERVALS (NODE STYLE)
def call_repeatedly(interval, func, *args): ## you can pass arguments too which is useful
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set
    

# check the weather once at startup
checkWeather()

# check the weather every 20 seconds
check_weather_timer = call_repeatedly(20, checkWeather) #seconds
