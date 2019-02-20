from os import listdir

Students = sorted(listdir("train/"))
StudentNames = [i.split("_") for i in Students]

