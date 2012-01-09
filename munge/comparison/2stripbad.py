# -*- coding: utf-8 -*-
import sys
fileopen = open(sys.argv[1], 'r')
fileout = open(str('cleaned' + sys.argv[1]), 'w')
words = ("a", "the", "at")
chars = ("!", ".", "?", "-", ":)", "!!!", ",", "(", ")", "£", "*", ";", "%", "$", '"')
badlist = []
linelist = []
for line in fileopen:
	linelist.append(line)
	for i in words:
		if line.startswith(i + "\t"):
			badlist.append(line)
	for el in chars:
		if el in line.strip():
			badlist.append(line)

print badlist

for i in linelist:
	if not i in badlist:
		fileout.write(i)