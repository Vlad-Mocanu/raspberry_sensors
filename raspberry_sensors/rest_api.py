#!flask/bin/python
import pymysql
import os
import glob
import time
import thread
import argparse
import json
from flask import Flask, jsonify, abort, request, make_response


app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--config_file', '-f', default="sensors_config.json", help='path to configuration json file (default: sensors_config.json)')
args = parser.parse_args()

with open(args.config_file) as data_file:
	config_options = json.load(data_file)
data_file.close()

def read_from_db(my_sql):
	db = pymysql.connect(host=config_options["mysql"]["server"],
						 user=config_options["mysql"]["user"],
						 passwd=config_options["mysql"]["password"])

	# an Cursor object must be created. It will let you execute all the queries you need
	cursor = db.cursor()

	try:
		# Execute the SQL command and commit changes in the database
		cursor.execute(my_sql)
		return cursor.fetchall()

	except:
		db.rollback()

	# disconnect from server
	db.close()

def prepare_json(table_name, where_string):
	sql = "show columns from " + config_options["mysql"]["database"] + table_name + ";"
	columns = read_from_db(sql)
	sql = "select * from " + config_options["mysql"]["database"] + table_name + " " + where_string + " order by id desc limit 1;"
	values = read_from_db(sql)
	result = {}
	for index in range(0, len(columns)):
		result[columns[index][0]] = values[0][index]
	return result
	

@app.route('/get_in_temp', methods=['GET'])
def get_indoor_temperature():
	results = [];
	results.append(prepare_json(".temperature", "where name=\"Indoor Living\""))
	return jsonify(results)

@app.route('/get_out_temp', methods=['GET'])
def get_outdoor_temperature():
	results = [];
	results.append(prepare_json(".temperature", "where name=\"Outdoor Unit\""))
	return jsonify(results)

@app.route('/get_humidity', methods=['GET'])
def get_humidity():
	results = [];
	results.append(prepare_json(".humidity", ""))
	return jsonify(results)

@app.route('/get_pressure', methods=['GET'])
def get_pressure():
	results = [];
	results.append(prepare_json(".pressure", ""))
	return jsonify(results)
	
@app.route('/get_windows', methods=['GET'])
def get_windows():
	results = [];
	for win in config_options["all_windows"]["window"]:
		results.append(prepare_json(".windows", "where name=\"" + win["name"] + "\""))
	return jsonify(results)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
