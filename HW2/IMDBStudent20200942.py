import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]

fi = open(inputfile)
fo = open(outputfile, "wt")
# f = open("movies_exp.txt")
a = dict()
for i in fi :
    s = i.split("::")
    genre = s[-1].split("|")

    for j.strip() in genre : 
        if j not in a :
            a[j.strip()] = 1
        else :
            a[j.strip()] += 1

for i, j in a.items() :
    line = i + " " + str(j) + "\n"
    fo.write(line)

fi.close()
fo.close()
