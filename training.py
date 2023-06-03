from char import *
def check(url):
    if 'http://' in url[:7]: url = httprem(url)
    if 'https://' in url[:8]: url = httpsrem(url)
    feature = 0
    checker = [
        atCheck(url), dotCount(url), HTTPCheck(url), slashCheck(url),
        sepCheck(url), tinyurl(url), redirectCheck(url)
    ]
    

    for i in checker:
        feature = i
        if feature:
            return 1
    return 0

'''
url=input("Enter URL : ")
if 'http://'in url[:7]:url= httprem(url)
if 'https://'in url[:8]:url= httpsrem(url)
print(url)
feature=0
checker=[
    atCheck(url),dotCount(url),HTTPCheck(url),slashCheck(url),slashCount(url),
    sepCheck(url),tinyurl(url),redirectCheck(url)
]

for i in checker:
    feature=i
    if feature:
        print('Phishing URL',checker.index(i))
        break
else:
    print("Legitimate URL")
'''