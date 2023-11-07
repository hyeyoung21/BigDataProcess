f = open("movie.dat")
# f = open("movies_exp.txt")
a = dict()
for i in f :
    s = i.split("::")
    genre = s[-1].split("|")

    for j in genre : 
        if j not in a :
            a[j.strip()] = 1
        else :
            a[j.strip()] += 1

for i, j in a.items() :
    print(i, j)

print(a)
