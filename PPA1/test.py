import a1
mydb, mycursor = a1.databaseCreation()

mycursor.execute('SELECT * FROM shortestDistance')
for x in mycursor:
	print(x)