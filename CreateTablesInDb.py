from DataBaseFunctions import *
"""
Creates tables in the initial database
"""
try:
	query = "create table TotalClasses(sno integer(3) AUTO_INCREMENT, cosmology integer(3), psychology integer(3), 		computerscience integer(3), botony integer(3), PRIMARY KEY(sno))"
	cursor.execute(query)
	query = "create table Attendance(sno integer(3) AUTO_INCREMENT,id varchar(20), name varchar(20), cosmology integer(3), 	psychology integer(3), computerscience integer(3), botony integer(3), PRIMARY KEY(sno))"
	cursor.execute(query)
	print("-----Tables Created-----\n")
except:
	print("Tables Already Created\n")

conn.commit()
