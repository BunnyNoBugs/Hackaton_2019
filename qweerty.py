import re

with open('pog.html', encoding = 'utf-8') as f:
    t = f.read()
    q = re.findall('<td>(.+?)</td>', t)
    
    print(q)
