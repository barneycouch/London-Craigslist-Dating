import re, os, sys
filelist = []
fullist = []
if len(sys.argv) != 2:
	print 'Please provide <source directory> input argument!'
	exit(1)
sys1 = (sys.argv[1])
rootdir = str(sys1)
for one, two, three in os.walk(rootdir):
	filelist.append(three)

for el in filelist:
	for i in el:
		if not 'index' in i:
			if not 'htmls' in i:
				if not i.startswith('.'):
					fullname = sys1 + '/' + i
					fullist.append(fullname)

body= []

for i in fullist:
	html = open(i, 'r')
	cnt = 0
	for line in html:
		line = line.replace("\n", "")
		line = line.replace("<br>", "")
		if line.startswith('<div id="userbody">'):
			cnt += 1
		if cnt == 1:
			if not line.startswith("<"):
				if not line.startswith('				<td'):
					if not line.startswith('	<li'):
						body.append(line)
		if line.startswith('<!-- START CLTAGS -->'):
			cnt = 0
	html.close()

fileout2 = open('../../cache/' + 'htmlparserout.txt', 'w')
	
for i in body:
	if len(i) >= 25:
		i = i.replace("<!-- START CLTAGS -->", "")
		fileout2.write('%s\n' % i)
			
fileout2.close()

