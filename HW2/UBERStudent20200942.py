import datetime
import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]

fi = open(inputfile)
fo = open(outputfile, "wt")
# f = open("uber_exp.txt")


wd = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
dict = dict()

for i in fi :
    s = i.split(",")
    car = s[0]
    date = s[1]
    vehicle = int(s[2])
    trip = int(s[3])
    
    d = date.split("/")
    month = int(d[0])
    day = int(d[1])
    year = int(d[2])
    w = datetime.datetime(year, month, day).weekday()
    weekday = wd[w]
    
    key = car + "," + weekday
    if key not in dict :
        dict[key] = str(vehicle) + "," + str(trip)
    else :
        s = dict[key].split(",")
        vehicle += int(s[0])
        trip += int(s[1])
        dict[key] = str(vehicle) + "," + str(trip)


for i, j in dict.items() :
    line = i + " " + j + "\n"
    fo.write(line)

fi.close()
fo.close()
