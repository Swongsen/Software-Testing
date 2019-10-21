from flask import Flask, url_for, request, jsonify
import mysql.connector

def databaseCreation(host='172.17.0.2', user='root', passwd='my-secret-pw'):
	try:
		mydb = mysql.connector.connect(
			host=host,
			user=user,
			passwd=passwd
		)

		mycursor = mydb.cursor()

		# Create DB if it doesn't exist
		mycursor.execute("CREATE DATABASE IF NOT EXISTS mydb")
		mycursor.execute("USE mydb")

		# Create tables if they don't exist
		mycursor.execute("CREATE TABLE IF NOT EXISTS shortestDistance(x1 FLOAT NOT NULL, y1 FLOAT NOT NULL, x2 FLOAT NOT NULL, y2 FLOAT NOT NULL, distance FLOAT NOT NULL, created_at TEXT NOT NULL)")
		mycursor.execute("CREATE TABLE IF NOT EXISTS bmi(height TINYTEXT NOT NULL, weight TINYTEXT NOT NULL, bmi TINYTEXT NOT NULL, classification TINYTEXT NOT NULL, created_at TEXT NOT NULL)")
		mycursor.execute("CREATE TABLE IF NOT EXISTS requests(table_name TINYTEXT NOT NULL, created_at TEXT NOT NULL)")

	except Exception as error:
		print('Database Initialization Error.\n' +
		 'Read the README, make sure the database has been started, and make sure the IP is correct.')
		print(error)
		return 0, 0
	return mydb, mycursor

app = Flask(__name__)
mydb, mycursor = databaseCreation()

@app.route('/bmi')
def api_bmi():
	mycursor.execute('SELECT * FROM bmi')
	row_headers = [x[0] for x in mycursor.description]
	results = mycursor.fetchall()
	json_data = []
	for result in results:
		json_data.append(dict(zip(row_headers,result)))

	mycursor.execute('INSERT INTO requests(table_name, created_at) VALUES (\'bmi\',NOW())')
	mydb.commit()
	return jsonify(json_data)

@app.route('/shortestDistance')
def api_shortestDistance():
	mycursor.execute('SELECT * FROM shortestDistance')
	row_headers = [x[0] for x in mycursor.description]
	results = mycursor.fetchall()
	json_data = []
	for result in results:
		json_data.append(dict(zip(row_headers,result)))

	mycursor.execute('INSERT INTO requests(table_name, created_at) VALUES (\'shortestDistance\',NOW())')
	mydb.commit()
	return jsonify(json_data)

@app.route('/requests')
def api_requests():
	mycursor.execute('SELECT * FROM requests')
	row_headers = [x[0] for x in mycursor.description]
	results = mycursor.fetchall()
	json_data = []
	for result in results:
		json_data.append(dict(zip(row_headers,result)))

	mycursor.execute('INSERT INTO requests(table_name, created_at) VALUES (\'requests\',NOW())')
	mydb.commit()
	return jsonify(json_data)

def run():
	app.run()
	print("Running")

if __name__ == '__main__':
	run()
