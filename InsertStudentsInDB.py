from DataBaseFunctions import *
from AllStudents import *
"""
Intializes the newly created tables by inserting all student details.
"""
query = "INSERT INTO TotalClasses (cosmology, psychology, computerscience, botony ) VALUES (0, 0, 0, 0)"
cursor.execute(query)
for i in StudentNames:
	query = "INSERT INTO Attendance (id, name, cosmology, psychology, computerscience, botony ) VALUES (%s, %s, 0, 0, 0, 0)"
	cursor.execute(query, i)
print("-----Inserted Successfully-----\n")
conn.commit()
