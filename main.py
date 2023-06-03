from char import *
from training import *

f=open('urls.txt',encoding="utf8")
g=open('features.txt',encoding='utf8')
temp=open('features.txt',encoding='utf8')
lc,pc=0,0

a=temp.readlines()
ulc=a.count('0\n')
upc=len(a)-ulc

s=f.readline()
t=g.readline()

while(s):
    if check(str(s)) and '1' in t:pc+=1
    elif check(str(s))==0 and '0' in t: lc+=1
    
    s=f.readline()
    t=g.readline()

print('Dataset Total :',ulc+upc)
print('Legitimate :',ulc)
print('Phishing :',upc)
print()

print('Program result total (correct):',lc+pc)
print('Legitimate :',lc)
print('Phishing :',pc)
print()

print('Wrong result total :',ulc+upc-lc-pc)
print('Legitimate :',ulc-lc)
print('Phishing :',upc-pc)
print()

print('Accuracy : %.2f\n'%(((lc+pc)/(ulc+upc))*100))

temp.close()
g.close()
f.close()