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

    for j in genre :
        movie = j.strip() 
        if movie not in a :
            a[movie] = 1
        else :
            a[movie] += 1
        # print(movie)

for i, j in a.items() :
    line = i + " " + str(j) + "\n"
    fo.write(line)

fi.close()
fo.close()
