from flask import Flask, request
import logging
from datetime import datetime
import pandas
import json

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

##add postgresql db and store results--add input sanintation
##can we communicate to the sensors!
 ##remore firmware update
 ##remote code deployment
##could we add sensor authentication?
##Add an endpoint to pull temperature data
##Build a frontend to display data
##stick on raspi
##host via howhotismyroom.com
##add functionality to assign nodes to room
##HTML canvas showing heat color per room?
##Temp last 10 seconds
##Temp Last hour
##Temp Last 3 hours
##Temp Last Day
##Temp Last week
##One temp chart class to pull different ranges
##Inputs time/Range + room
##Animation of color change over time?
##get Nodes to talk to remote server

##store results in DB

def hello_world():
    return 'Hello World!'

def log_data(log):
    log=str(log)
    log_file=open(r"sensor_log.txt","a")
    log_file.write('\n'+log)
    app.logger.info('The Following Log Has Been Recorded %s'%log)

@app.route('/sensor_exception', methods=['POST'])
def sensor_exception():
    app.logger.info("Exception Occured In Temp Station")
    data = request.get_json(force=True)
    station_id = data['station_id']
    error_msg = data['status']
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
    error_log = {'station_id': station_id, 'status': error_msg, 'timestamp': timestamp}
    app.logger.info('The Following Dict Has Been Recorded %s' % data)
    log_data(error_log)
    return error_log

@app.route('/get_temp',methods=['GET'])
def get_temp():
    



@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.get_json(force=True)
    temp = data['temp']
    station_id = data['station_id']
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
    uploaded_dict = {'status': 'uploaded', 'temp': temp, 'station_id': station_id, 'request_received at': timestamp}
    app.logger.info('The Following Dict Has Been Recorded %s' % data)
    log_data(uploaded_dict)
    return uploaded_dict


if __name__ == '__main__':
    app.run()
