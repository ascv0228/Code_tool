from functools import singledispatch
from collections import namedtuple
import re

class 


Post_Url = namedtuple('Post_Url',['php','page','bsn','snA'])
PHP, PAGE, BSN, SNA='C.php?', 1, None, None

def sscanf(s,format):
    m = re.match(format, s)
    if m:
        return list(m.groups())

@singledispatch
def dict_to_url(*s):
    print(f' 傳輸參數類型為：{type(s)}，不是有效類型')

@dict_to_url.register
def _(s: dict):
    global PHP, PAGE, BSN, SNA
    default_post_url = Post_Url(PHP, PAGE, BSN, SNA)
    PHP, PAGE, BSN, SNA = (output:=default_post_url._replace(**s))
    return output

@dict_to_url.register
def _(s: str):
    format = r'https://forum.gamer.com.tw/(.*)page=(.*)&bsn=(.*)&snA=(.*)'
    if (tup1 := sscanf(s,format)) == None:
        return
    names = 'php','page','bsn','snA'
    return dict_to_url({name:value for name, value in zip(names, tup1)})




print(dict_to_url('1'))
print(dict_to_url({'page':5}))
print(dict_to_url({'bsn':8,'snA':100}))
print(dict_to_url('https://forum.gamer.com.tw/Co.php?page=1&bsn=60076&snA=6327426'))
