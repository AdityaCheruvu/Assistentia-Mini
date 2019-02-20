from test import *
from DataBaseFunctions import  *
from AllStudents import *
from subprocess import call

"""
Main file which drives all the application utility files
"""
print("\nChoose an option:\n1 - Mark Attendance\n2 - Get Student Details\n")
ch = int(input())

def takeAttendance():
	"""
	Function to take attendance. This is called only once per execution.
	"""
	print("Enter Subject: ")
	subject = input()
	a=set()
	for image_file in os.listdir("test"):
		full_file_path = os.path.join("test", image_file)
		predictions = predict(full_file_path, model_path="trained_knn_model.clf")
		for name, (top, right, bottom, left) in predictions: 
			if(str(name)!="unknown"):
				a.add(str(name));
	MarkAttendance(list(a), subject)
	absentees = ReturnAbsentList(list(a))
	print("\nAnsentees are: ")
	print(absentees)
	announceAbsentees(absentees)
	print("\nEnter id's of the student's who are marked absent mistakenly if any else press enter: ")
	inp = input()
	wa=[]
	inp = ''.join(inp.split())
	wa = inp.split(",")
	if(len(wa) > 0):
		call(["espeak", "Sorry! I will try not to make that mistake again! It is advised that you keep your face straight while I take attendance. Thank you"])
	MarkAttendance(wa, subject)

def announceAbsentees(absentees):
	"""
	Dependent on espeak linux package. 
	Used announce absentees through text-speech using a speaker.
	"""
	call(["espeak", "Absentees list are, "])
	for i in absentees: 	
		call(["espeak", i[1]+", "])
if(ch == 1):
	takeAttendance()

elif(ch == 2):
	print("\nChoose an option\n1 - Get all student's attendance\n2 - Get attendance details of selected students\n")
	op = int(input())
	if(op == 1):
		try:
			GetDetails(Students)
		except:
			print("No Student found")
	elif(op == 2):
		print("\nChoose an option\n1 - Enter Student Id's\n2 - Give Input Image\n")
		opt = int(input())
		if(opt == 1):	
			print("\nEnter Student's Ids List: ")
			students=[]
			inp = input()
			inp = ''.join(inp.split())
			students = inp.split(",")
		elif(opt == 2):	
			print("Give the path of the image: ")
			full_file_path = input()
			a1=set()
			predictions = predict(full_file_path, model_path="trained_knn_model.clf")
			for name, (top, right, bottom, left) in predictions: 
				if(str(name)!="unknown"):
					a1.add(str(name));
			students = list(a1)

		GetDetails(list(students))
			
	else:	
		print("\nInvalid option entered...")
else:	
	print("\nInvalid option entered...")

