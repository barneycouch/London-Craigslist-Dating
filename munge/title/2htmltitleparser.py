import re, sys
titlelist = []
if len(sys.argv) != 2:
	print 'Please provide the file to parse!'
	exit(1)
htmls = sys.argv[1]

sysarg = sys.argv[1].split('/')
filedir = sysarg[:-1]
filedirpath = '/'.join(filedir) + '/'

openfile = open(htmls, 'r')
fileoutname = filedirpath + 'titles.txt'
titles = open(fileoutname, 'w')
for line in openfile:
	if line.startswith('	<title>'):
		line = line.replace("<title>", "")
		line = line.replace("</title>", "")
		line = line.replace("\n", "")
		line = line.replace("\t", "")
		line = line.replace("&", "")
		line = line.replace("'", "")
		titles.write(line)
		titles.write('\n')
		
openfile.close()