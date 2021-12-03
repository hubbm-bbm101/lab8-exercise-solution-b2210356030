import sys
f = open(sys.argv[1], encoding="utf-8")
dict1 = {}
for i in f:
    i = i.replace("\n", "")
    x, school = i.split(":")
    dict1[x] = str(school)
for student in sys.argv[2].split(","):
    try:
        print("Name: {}, University: {}".format(student, dict1[student]))
    except:
        print("{} was not found!".format(student))