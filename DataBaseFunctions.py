from AllStudents import *
import mysql.connector
conn=mysql.connector.connect(user='root', password='toor', host='localhost', database="Mini_Proj")
cursor = conn.cursor()

def UpdateTotalClasses(sub):
	"""
	Increments the total number of classes taken for a subject in the database
	"""
	query = "update TotalClasses set %s=%s+1 where sno=1"%(sub,sub)
	cursor.execute(query)
	conn.commit()

def ReturnAbsentList(Present):
	"""
	Utility function to return a list of absentees, by taking the list of presentees
	"""
	print("\nPresentees are:\n")
	print(Present)
	absentees = list(set(["_".join(i) for i in StudentNames]) - set(Present))
	absentees = [i.split("_") for i in absentees]
	return absentees

def GetDetails(stu):
	"""
	Utility function to retrieve student details for a given set of students
	"""
	for i in stu:
		query = "select * from Attendance where id = '%s'"%(i.split("_")[0])
		cursor.execute(query)
		print("\nStudent %s Details: "%(i.split("_")[0]))
		details = cursor.fetchall()[0]
		print("Roll No: " + details[1])
		print("Name: " + details[2])
		subs = getSubjects()
		for i in range(len(subs[3:])):
			print(subs[3+i][0] + ": " + str(details[3+i]))
		
		

def MarkAttendance(l,sub):
	"""
	function to mark attendance for a given list of students l, for a given subject sub
	"""
	UpdateTotalClasses(sub)
	for i in l:
		query = "update Attendance set %s=%s+1 where id='%s'"%(sub, sub, i.split("_")[0])
		cursor.execute(query)
	print("-----Attendance Details Updated-----\n")	
	conn.commit()
conn.commit()

def getSubjects():
	"""
	Retrieves a set of subjects from the database
	"""
	query = 'SELECT COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="Attendance"'
	cursor.execute(query)
	return cursor.fetchall()















