import sys
res1f = sys.argv[1]
res2f = sys.argv[2]
res3f = sys.argv[3]
res4f = sys.argv[4]
res1 = open(res1f, 'r')
res2 = open(res2f, 'r')
res3 = open(res3f, 'r')
res4 = open(res4f. 'r')
fileout = open('anal.txt', 'w')
fileout.write('%s\t%s\t%s\n' % ('Word',res1f[:4], res2f[:4], res3f[:4]. res4f[:4]))
r1dic = {}
r2dic = {}
r3dic = {}
r4dic = {}
for line in res1:
	line = line.replace('\n', '')
	word, cnt = line.split('\t')
	r1dic[word] = cnt

for line in res2:
        line = line.replace('\n', '')
        word, cnt = line.split('\t')
        r2dic[word] = cnt

for line in res3:
        line = line.replace('\n', '')
        word, cnt = line.split('\t')
        r3dic[word] = cnt

for line in res4:
        line = line.replace('\n', '')
        word, cnt = line.split('\t')
        r4dic[word] = cnt

for word in r1dic:
	dic1 = r1dic[word]
	if word in r2dic:
		dic2 = r2dic[word]
		if word in r3dic:
			dic3 = r3dic[word]
			if word in r4dic:
				dic4 = r4dic[word]
			if not word in r4dic:
				dic4 = '0'
		if not word in r3dic:
			dic3 = '0'
			if word in r4dic:
                                dic4 = r4dic[word]
                        if not word in r4dic:
                                dic4 = '0'
	if not word in r2dic:
		dic2 = '0'
		if word in r3dic:
                        dic3 = r3dic[word]
			if word in r4dic:
                                dic4 = r4dic[word]
                        if not word in r4dic:
                                dic4 = '0'
                if not word in r3dic:
                        dic3 = '0'
			if word in r4dic:
                                dic4 = r4dic[word]
                        if not word in r4dic:
                                dic4 = '0'
	fileout.write('%s\t%s\t%s\t%s\n' % (word, dic1, dic2, dic3, dic4))

#for word in r2dic:
#	if not word in r1dic:
#		dic1 = 0
#		dic2 = r2dic[word]
#		fileout.write('%s\t%s\t%s\n' % (word, dic1, dic2))


fileout.close()
