def get_weather():
	api_key = "de814eebff0d9713ef2b8fe437f4577c"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=Warszawa"
	response = requests.get(complete_url)
	return response.json()

def queue():
	threading.Timer(5.0, queue).start()
	url = os.environ.get('rabbitmq', 'amqp://guest:guest@localhost/%2f')
	params = pika.URLParameters(url)
	params.socket_timeout = 5
	connection = pika.BlockingConnection(params) # Connect to CloudAMQP
	channel = connection.channel() # start a channel
	weather = get_weather()
	channel.basic_publish(exchange='data_exchange', routing_key='data_queue', body=str(weather["main"]["temp"]))
	connection.close()

queue()
