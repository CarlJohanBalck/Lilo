import flask_cors
from flask import Flask, request
import configparser
from flask_cors import CORS

from datetime import datetime, date, timedelta
import json


from config import (
    IP_ADDRESS,   
	PORT_FE,
	
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

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=PORT_FE, use_reloader=True)
	