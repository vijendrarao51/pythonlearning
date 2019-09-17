# Weather Reporting System 
# Author : Vijendra Rao
# Date : 17 Sep 2019

import requests
import pprint

def get_weather_report(cityquery) :
	request_param = {'q' : cityquery, 'appid' : '4245d104bd4deda53b20e79e231e8f47', 'units' : 'metric'}
	url = 'http://api.openweathermap.org/data/2.5/weather'
	weather_data = requests.get(url, request_param)
	weather_json = weather_data.json()
	return weather_json


def main() :
	print("*****************************************")
	print("**                                     **")
	print("** Welcome to Weather Reporting System **")
	print("**                                     **")
	print("*****************************************")

	while(True) :
		user_city = input("Enter the city name (,country code) [Enter Q to quit]: ")
		if user_city.upper() == 'Q' :
			break
		weather_json = get_weather_report(user_city)
		if weather_json['cod'] != 200 :
			print("We are not able to find the city '"+ user_city + "'. Try Again!")
		else :
			print("Weather Report for " + weather_json['name'] + ", " + weather_json['sys']['country'])
			print("Weather : "+ weather_json['weather'][0]['description'])
			print("Wind Speed : "+ str(weather_json['wind']['speed']) + " meter/sec at " + str(weather_json['wind']['deg']) + " degree")
			print("Minimum Temp : ", weather_json['main']['temp_min'], "degree Celsius")
			print("Mixium Temp : ", weather_json['main']['temp_max'], "degree Celsius")
			print("Humidity : ", weather_json['main']['humidity'], "%")

main()