import time
from datetime import datetime, date, timedelta
from tkinter import E
import socket
import time
import configparser
import calendar
from sense_hat import SenseHat
import os
from decimal import *
from threading import Thread
from flask import Flask
from flask_cors import CORS



from config import (
	IP_ADDRESS,
	PORT,
	needs_water,
	got_water,
	running,
	swimming,
	gym
)


monday = 0
tuesday = 1
wednesday = 2
thursday = 3
friday = 4
saturday = 5
sunday = 6
hasTrained = False


hostname = socket.gethostname()
ip_address = IP_ADDRESS
app = Flask(__name__)
CORS(app)

print('\n Hostname of your Pi: ' + hostname)
print(' IP address of Pi: ' + ip_address)

sense = SenseHat()


def received_water(event):
	if event.action == 'pressed':
		LiloFick()

def received_training(event):
	if event.action == 'pressed':
		global hasTrained
		hasTrained = True
		
def LiloWaterLight():
	config = configparser.ConfigParser()
	config.read('lastDate_water.ini')
	now = datetime.now() # current date and time	
	date_time = now.strftime("%d/%m/%Y")

	while True:
		sense.stick.direction_middle = received_water
		sense.stick.direction_right = received_training
		try:
			config = configparser.ConfigParser()
			config.read('lastDate_water.ini')
			lastDate = config['DEFAULT']['last_water'].split(' ', 1)[1]
			now = datetime.now() # current date and time	
			date_time = now.strftime("%d/%m/%Y")
			
			date_format = "%d/%m/%Y"
			a = datetime.strptime(date_time, date_format)
			b = datetime.strptime(lastDate, date_format)
			delta = a - b
			sense.set_rotation(180)
			number = 0
			if(delta.days > 0):
				number = needs_water
			else:
				number = got_water
				if(now.weekday() == monday and (not hasTrained)):
					number = gym
				if(now.weekday() == tuesday and (not hasTrained)):
					number = running
				if(now.weekday() == thursday and (not hasTrained)):
					number = swimming
				else:
					number = got_water

			sense.set_pixels(number)
		except AttributeError:
			time.sleep(2)
			continue
	
	
def LiloFick():
	now = datetime.now() # current date and time	
	date_time = now.strftime("%d/%m/%Y")	
	config = configparser.ConfigParser()
	my_date = date.today()
	weekday = calendar.day_name[my_date.weekday()]
	config.read('lastDate_water.ini')
	config['DEFAULT']['last_water'] = weekday + " " + date_time
	config['DEFAULT']['last_water_time'] = now.strftime("%H:%M")
	with open('lastDate_water.ini', 'w') as configfile:
		config.write(configfile)

if __name__ == '__main__':
	thread = Thread(target = LiloWaterLight)
	thread.start()
	app.run(debug=True, host=ip_address, port=PORT, use_reloader=False)