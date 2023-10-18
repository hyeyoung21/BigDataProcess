#!/usr/bin/python3
from openpyxl import load_workbook

wb = load_workbook(filename = 'student.xlsx')
s = wb['Sheet1']

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
	s['G' + str(i)] = s[mid].value * 0.30 + s[final].value * 0.35 + s[hw].value * 0.34 + s[att].value
		
	list.append(s[total].value)
	i += 1

list.sort()
print(list)

#mid 30 final 35 hw 34 att 1​