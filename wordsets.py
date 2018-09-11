import os
import time
import re

'''
print(os.path.getsize('D://nlp//noword.txt'))
#fp = open("D://nlp//noword.txt")
#frl = fp.readline()
#sdd = re.search(r'.*国',frl.strip('\n'))
#print(len(fp.read()))
'''

# 将文件夹中，各文件的内容回合到文件2014904.txt中

for foldername in os.listdir('D://nlp//2014//'):
    fp1 = open('D://nlp//2014904'+str(foldername)+'.doc', 'w+', encoding='GBK')
    print(foldername)
    for filename in os.listdir('D://nlp//2014//' + str(foldername)+'//'):
        pa = 'D://nlp//2014//' + str(foldername)+'//'+str(filename)
        fp = open(pa, 'r', encoding='utf-8')
        for line in fp.readlines():
            fp1.write(line)
        fp.close()
    time.sleep(2)
    fp1.close()


fp = open("D://nlp//2014904.txt", 'r+', encoding="GBK")
fp1 = open("D://nlp//2014sub.txt", 'w+', encoding='GBK')
for file in fp.readlines():
    #con = re.findall('后天/([a-z])', file)
    midlin = re.sub(r'后天/([a-z])', "后天/t", file)
    fp1.write(midlin)
    #if con:
     #print(con)
fp.close()
fp1.close()
