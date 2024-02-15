import flask_cors
from flask import Flask, request
import configparser
from flask_cors import CORS

from datetime import datetime, date, timedelta
import json
import subprocess

import calendar

from config import (
    IP_ADDRESS,   
	PORT_BE,
	
)
ip_address = IP_ADDRESS
app = Flask(__name__)
CORS(app)

@app.route('/Status', methods=['GET'])
def GetStatus():
    config = configparser.ConfigParser()
    config.read('lastDate.ini')
    lastDate = config['DEFAULT']['last_date'].split(' ', 1)[1]
    now = datetime.now() 
    date_time = now.strftime("%d/%m/%Y")	
    date_format = "%d/%m/%Y"
    a = datetime.strptime(date_time, date_format)
    b = datetime.strptime(lastDate, date_format)
    delta = a - b
    response = []

    if delta.days == 0:
        response.append(False)
        response.append(delta.days)
        response.append(lastDate)
        return json.dumps(response)
    elif (delta.days % 2) == 0:
        response.append(True)
        response.append(delta.days)
        response.append(lastDate)
        return json.dumps(response)
    else:  
        response.append(False)
        response.append(delta.days)
        response.append(lastDate)
        return json.dumps(response)
    
@app.route('/LiloFick', methods=['POST'])
def LiloGot():
     LiloFickBe()
     response = ["200"]
     return json.dumps(response)


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=PORT_BE, use_reloader=True)
	
def LiloFickBe():
	now = datetime.now() # current date and time	
	date_time = now.strftime("%d/%m/%Y")	
	config = configparser.ConfigParser()
	my_date = date.today()
	weekday = calendar.day_name[my_date.weekday()]
	config.read('lastDate.ini')
	config['DEFAULT']['last_date'] = weekday + " " + date_time
	with open('lastDate.ini', 'w') as configfile:
		config.write(configfile)
	subprocess.call(['sh', '/home/pi/code/scripts/push_lilo.sh'])
	