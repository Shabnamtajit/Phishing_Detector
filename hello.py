from char import *
from training import *

f=open('urls.txt','+r', encoding="utf8")
g=open('features.txt','+r', encoding='utf8')

lc,pc=0,0

endp=86349
endl=24516

s=f.readline()
t=g.readline()

while(s):
    if check(str(s)):
        if '1' in t:pc+=1
        elif endl>7946:
            f.write('')
            g.write('')
            endl-=1
            
    elif check(str(s))==0:
        if '0' in t: lc+=1
        elif endp>5981:
            f.write('')
            g.write('')
            endp-=1
            
    s=f.readline()
    t=g.readline()
    
print(lc,pc)