import ipaddress

def httprem(s):
    return s[7:]

def httpsrem(s):
    return s[8:]
def atCheck(s):
    if '@' in s: return 1
    return 0

def HTTPCheck(s):
    if 'HTTP' in s:return 1
    return 0

def dotCount(s):
    a=s[:s.index('/')] if '/' in s else s
    if a.count('.')>3:return 1
    return 0

def sepCheck(s):
    a = s[:s.index('/')] if '/' in s else s
    if '-' in a: return 1
    return 0

def colonCheck(s):
    if ':'  in s: return 1
    return 0

def slashCheck(s):
    if '//' in s:return 1
    return 0

def tinyurl(s):
    if 'bit.ly' in s:return 1
    return 0

def urllenCheck(s):
    a = s.index('/') if '/' in s else len(s)
    if a>25:return 1
    return 0

def redirectCheck(s):
    a = s[s.index('/'):] if '/' in s else s
    if 'http' in a:return 1
    return 0

def ipCheck(s):
    try:
        ipaddress.ip_address(s)
        return 1
    except:
        return 0
    
def urllencheck(s):
    a = s.index('/') if '/' in s else len(s)
    if a>54:return 1
    return 0
