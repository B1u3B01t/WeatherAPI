import urllib.request #importing module urllib.request
import datetime #importing module datetime
def weather_response(location, API_key):#Function for getting the json string
	url =urllib.request.urlopen('url till location'+location+'&APPID='+API_key)
	json = url.read()#.decode('utf-8')
	return str(json)
def has_error(json,location): #has error or not
	json=str(json)
	if json == str(b'{"cod":"404","message":"city not found"}'):
		print("error 404,city not found")
		return None
	else:
		name = json.rfind('"name"')
		city_start = name+7
		city_end = json.rfind(',',city_start)
		city_end = city_end -1
		city = json[city_start:city_end]
		if city.lower() == location.lower() :
			return True
		else:
			return False
def get_temperature(json,n=0,t='03:00:00'):
	date = (datetime.datetime.now().date())+ (datetime.timedelta(days =n))
	date = str(date)
	t = date+' '+t
	date_find = json.find(t)
	sliced_1  = json[:date_find]
	temp_find = sliced_1.rfind('"temp"')
	temp_index = temp_find + 7
	finding_comma = sliced_1.find(',',temp_index)
	temp = sliced_1[temp_index:finding_comma]
	temp = float(temp)
	return temp	
def get_humidity(json,n=0,t='03:00:00'):
	date = (datetime.datetime.now().date())+ (datetime.timedelta(days =n))
	date = str(date)
	t = date+' '+t
	date_find = json.find(t)
	sliced_1  = json[:date_find]
	humidity_find = sliced_1.rfind('humidity')
	humidity_index = humidity_find + 10
	finding_comma = sliced_1.find(',',humidity_index)
	humidity = sliced_1[humidity_index:finding_comma]
	humidity = float(humidity)
	return humidity
def get_pressure(json,n=0,t='03:00:00'):
	date = (datetime.datetime.now().date())+ (datetime.timedelta(days =n))
	date = str(date)
	t = date+' '+t
	date_find = json.find(t)
	sliced_1  = json[:date_find]
	pressure_find = sliced_1.rfind('"pressure"')
	pressure_index = pressure_find + 11
	finding_comma = sliced_1.find(',',pressure_index)
	pressure = sliced_1[pressure_index:finding_comma]
	pressure = float(pressure)
	return pressure
def get_sealevel(json,n=0,t='03:00:00'):
	date = (datetime.datetime.now().date())+ (datetime.timedelta(days =n))
	date = str(date)
	t = date+' '+t
	date_find = json.find(t)
	sliced_1  = json[:date_find]
	sea_level_find = sliced_1.rfind('"sea_level"')
	sea_level_index = sea_level_find + 12
	finding_comma = sliced_1.find(',',sea_level_index)
	sea_level = sliced_1[sea_level_index:finding_comma]
	sea_level = float(sea_level)
	return sea_level
def get_wind(json,n=0,t='03:00:00'):
	date = (datetime.datetime.now().date())+ (datetime.timedelta(days =n))
	date = str(date)
	t = date+' '+t
	date_find = json.find(t)
	sliced_1  = json[:date_find]
	wind_find = sliced_1.rfind('"wind"')
	wind_index = wind_find + 16
	finding_comma = sliced_1.find(',',wind_index)
	wind = sliced_1[wind_index:finding_comma]
	wind = float(wind)
	return wind
