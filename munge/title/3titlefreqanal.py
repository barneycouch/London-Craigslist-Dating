import sys
from collections import Counter
if len(sys.argv) != 2:
	print 'Please provide the file to analyse!'
	exit(1)
titles = sys.argv[1]

sysarg = sys.argv[1].split('/')
filedir = sysarg[:-1]
filedirpath = '/'.join(filedir) + '/'


freqout = open((filedirpath + 'titlefreqanalout.txt'), 'w')
fileopen = open(sys.argv[1], 'r')
wordlist = []
for line in fileopen:
	line = line.split()
	wordlist.append(line)
	
	
cnt = Counter()

for word in wordlist:
	for i in word:
		i = i.lower() #makes everything lowercase
		cnt[i] += 1

for word, cnt in cnt.most_common(300):
	freqout.write('%s\t%s\n' % (word, cnt))

fileopen.close()
freqout.close()