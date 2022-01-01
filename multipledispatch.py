from functools import singledispatch
from multipledispatch import dispatch
from collections import namedtuple
import re

class BahamutPost:
    Post_Url = namedtuple('Post_Url',['php','page','bsn','snA'])
    PHP, PAGE, BSN, SNA = 'C.php?', 1, None, None
    
    def __init__(self, urlInfo, outputOrder = (), control = [True]*4):
        self.isIncludeEdit, self.isIncludeRepeat, self.isIncludeDelete, self.isIncludeFolded = control
        self.outputOrder = outputOrder
        self.outputList = []
        self.PHP, self.PAGE, self.BSN, self.SNA = PHP, PAGE, BSN, SNA
        
    @dispatch(object)
    def dict_to_url(self, *arg):
        print(f' 傳輸參數類型為：{type(s)}，不是有效類型')

    @dispatch(dict)
    def dict_to_url(self,s):
        global PHP, PAGE, BSN, SNA
        default_post_url = Post_Url(PHP, PAGE, BSN, SNA)
        PHP, PAGE, BSN, SNA = (output:=default_post_url._replace(**s))
        return output

    @dispatch(str)
    def dict_to_url(self,s):
        format = r'https://forum.gamer.com.tw/(.*)page=(.*)&bsn=(.*)&snA=(.*)'
        if (tup1 := sscanf(s,format)) == None:
            return
        names = Post_Url._fields
        return dict_to_url({name:value for name, value in zip(names, tup1)})    
    
    

def sscanf(s,format):
    m = re.match(format, s)
    if m:
        return list(m.groups())

url='https://forum.gamer.com.tw/Co.php?page=1&bsn=60076&snA=6327426'
a = BahamutPost(url)



print(a.dict_to_url('1'))
print(a.dict_to_url({'page':5}))
print(a.dict_to_url({'bsn':8,'snA':100}))
print(a.dict_to_url('https://forum.gamer.com.tw/Co.php?page=1&bsn=60076&snA=6327426'))
