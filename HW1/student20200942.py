#!/usr/bin/python3
from openpyxl import load_workbook
from openpyxl import Workbook

wb1 = load_workbook(filename = 'student.xlsx')
s = wb1['Sheet1']


i = 2
list = []
mid = 'C' + str(i)
while s[mid].value != None :
	mid = 'C' + str(i)
	final = 'D' + str(i)
	hw = 'E' + str(i)
	att = 'F' + str(i)
	
	if s[mid].value == None : break
    
	total = 'G' + str(i)
	s[total] = s[mid].value * 0.30 + s[final].value * 0.35 + s[hw].value * 0.34 + s[att].value
		
	list.append(s[total].value)
	i += 1

list.sort()
list.reverse()
print(list)

i -= 2

ap = int(i * 0.15)
a = int(i * 0.3)
bp = int(i * 0.5)
b = int(i * 0.7)
cp = int(i * 0.85)

for j in range(2, i) :
	total = s['G' + str(j)].value
	grade = 'H' + str(j)
	if total <= 40 :
		s[grade] = "F"
	elif total > list[ap] : 
		s[grade] = "A+"
	elif total > list[a] :
		s[grade] = "A"
	elif total > list[bp] :
		s[grade] = "B+"
	elif total > list[b] :
		s[grade] = "B"
	elif total > list[cp] :
		s[grade] = "C+"
	else :
		s[grade] = "C"
	print(grade +" "+ s[grade].value)

wb1.save('student.xlsx')
wb1.close()
		 
#mid 30 final 35 hw 34 att 1​
