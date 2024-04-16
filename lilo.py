import os
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
from flask import Flask, request
from flask_cors import CORS
import subprocess


from config import (
	IP_ADDRESS,
	PORT,
	smiley_face,
	g1,
	g2,
	g3,
	g4,
	r1,
	r2,
	r3,
	r4
)

hostname = socket.gethostname()
ip_address = IP_ADDRESS
app = Flask(__name__)
CORS(app)


sense = SenseHat()

def getEverySecondDateInFuture(date):
	parsedDate = datetime.strptime(date, "%d/%m/%Y").date()
	dateList = []
	for i in range (20):
		td = timedelta(days=i+2)
		futureDate = parsedDate + td
		futureMedicationDates = futureDate.strftime("%d/%m/%Y")	
		dateList.append(futureMedicationDates)
	everyOtherDateList = dateList[::2]
	return everyOtherDateList

def received_medicine(event):
	if event.action == 'pressed':
		LiloFick()
		
def LiloStatusLight():
	config = configparser.ConfigParser()
	config.read('lastDate.ini')
	now = datetime.now() # current date and time	
	date_time = now.strftime("%d/%m/%Y")
	last_date = config['DEFAULT']['last_date']
	last_date_parsed = last_date.split(" ")[1]
	futureMedicationDates = getEverySecondDateInFuture(last_date_parsed)

	if date_time in futureMedicationDates: 
		while True:
			sense.stick.direction_middle = received_medicine
			try:
				config = configparser.ConfigParser()
				config.read('lastDate.ini')
				lastDate = config['DEFAULT']['last_date'].split(' ', 1)[1]
				now = datetime.now() # current date and time	
				date_time = now.strftime("%d/%m/%Y")	
				date_format = "%d/%m/%Y"
				a = datetime.strptime(date_time, date_format)
				b = datetime.strptime(lastDate, date_format)
				delta = a - b
				sense.set_rotation(180)

				number = 0
				
				if(delta.days == 1):
					number = g1
				elif (delta.days == 2):
					number = g2
				elif (delta.days == 3):
					number = g3
				elif (delta.days == 4):
					number = g4
				elif(delta.days == 0):
					number = smiley_face
				sense.set_pixels(number)
			except AttributeError:
				time.sleep(2)
				continue
	else: 
		while True:
			sense.stick.direction_middle = received_medicine
			try:
				config = configparser.ConfigParser()
				config.read('lastDate.ini')
				lastDate = config['DEFAULT']['last_date'].split(' ', 1)[1]
				now = datetime.now() # current date and time	
				date_time = now.strftime("%d/%m/%Y")	
				date_format = "%d/%m/%Y"
				a = datetime.strptime(date_time, date_format)
				b = datetime.strptime(lastDate, date_format)
				delta = a - b
				sense.set_rotation(180)
				number = 0
				if(delta.days == 1):
					number = r1
				elif (delta.days == 2):
					number = r2
				elif (delta.days == 3):
					number = r3
				elif (delta.days == 4):
					number = r4
				elif(delta.days == 0):
					number = smiley_face

				sense.set_pixels(number)
				
			except AttributeError:
				time.sleep(2)
				continue
	
	
def LiloFick():
	now = datetime.now() # current date and time	
	date_time = now.strftime("%d/%m/%Y")	
	config = configparser.ConfigParser()
	my_date = date.today()
	sense = SenseHat()
	weekday = calendar.day_name[my_date.weekday()]
	config.read('lastDate.ini')
	config['DEFAULT']['last_date'] = weekday + " " + date_time
	with open('lastDate.ini', 'w') as configfile:
		config.write(configfile)
	# subprocess.call(['sh', '/home/pi/code/scripts/push_lilo.sh'])
	# sense.set_pixels(smiley_face)

	process = subprocess.Popen(['sh', '/home/pi/code/scripts/push_lilo.sh'])

	# Check if the subprocess has finished
	if process.poll() is None:
		print("Subprocess is still running.")
	else:
		print("Subprocess has finished.")
		sense.set_pixels(smiley_face)


if __name__ == '__main__':
	thread = Thread(target = LiloStatusLight)
	thread.start()
	app.run(debug=True, host=ip_address, port=PORT, use_reloader=False)