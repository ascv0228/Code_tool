# your code goes here
import re

def sscanf(str_, format_, *args):
    try:
        m = re.match(format_, str_)
    except:
        return
    m = m.groups()
    if args == ():
        return list(m)    
    for list_ in args:
        list_.clear()
    if len(args) == 1:
        args[0].extend(list(m))
    elif len(args) == len(m):
        for i in range(len(args)):
            args[i].extend([m[i]])
    else:
        raise TypeError
    return list(m)



input_str = 'an apple, an orange, and a banana'
const_format = r'an (.*), an (.*), and a (.*)'
print('======================================================================')
s = [12345]
t = [555]
u = ['qwe']
print('======================================================================')
print(sscanf(input_str,const_format))             # given 0 arg = only return
print('======================================================================')
print(sscanf(input_str,const_format,s))           # given 1 arg = return, and full-coverage
print(s)
print('======================================================================')
print(sscanf(input_str,const_format,s,t,u))       # given n (n == len(return)) arg = return, and sequential-coverage
print(s,t,u)
print('======================================================================')
print(sscanf(input_str,const_format,s,t))         # given n (n != len(return)) arg = TypeError
print(s,t)
print('======================================================================')
input_str = None
print(sscanf(input_str,const_format,s,t,u))         # given error input_str = None
print(s,t,u)
