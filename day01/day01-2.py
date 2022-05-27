#方法1
s = "i,am,lilei"
temp = s.split(',')
temp.pop(temp.index("am"))
s = ',,'.join(temp)
#方法2
s = "i,am,lilei"
ss = ''
for i in s:
    if i!= 'a' and i != 'm':
        ss += i
s = ss
