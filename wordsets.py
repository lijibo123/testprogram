import os
import time
import re
'''
print(os.path.getsize('D://nlp//noword.txt')) but GitHub does not provide shell access.
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
'''
# 此部分添加了有关时间测试的函数
import time
start_time = time.time()
pass
end_time = time.time()
print(end_time - start_time)
'''
# 该部分为自定义字段中的数据预处理部分的程序
import pickle
import os
import pandas as pd
import re
pattern = re.compile(r'(\（(.*)\）)|(\d.*$)|(\((.*)\))') #匹配模式有三种，名字后有中文括号、英文括号、数字及数字和字母
df = pd.read_excel('D://program file//user.xlsx') # 所有名字集合的读取
allname = df['real_name']
listname = []
setname = set(allname) # 基于集合去除名字存在的重复情况。
for na in setname:
    midstr = pattern.sub('', na)
    listname.append(midstr)
setname = set(listname) # 二次去重
pickle.dump(setname,open(os.path.join(os.getcwd(),'x'),'wb')) # 存储以备用