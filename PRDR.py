#只支持字符串、数字、列表、字典等类型
from sys import argv
from tkinter import Tk,Text,Label
from pickle import load
from _collections_abc import Iterable

try:
    read_file_name=argv[1]
except IndexError:
    w=Tk()
    w.geometry('220x120')
    w.title('错误')
    Label(w,text='未打开文件',font=(None,20),fg='red').pack()
    w.mainloop()
    exit()

f=open(read_file_name,'rb')
content=load(f)

content_type=str(type(content))
if isinstance(content,Iterable):
    temp=content
    content=''
    if type(temp)==type(dict()):
        temp=temp.items()
    for i in temp:
        if type(i)==type(''):
            content+='"'+i+'"'
        else:
            content+=str(i)
        content+='\n'
else:
    content=str(content)
w=Tk()
w.title('pickle阅读器')
w.geometry('1200x400')
showt_t=Text(w,width=150,height=1)
showc_t=Text(w,width=150)
showc_t.insert('end',content)
showt_t.insert('end',content_type)

showc_t.config(state='disabled')
showt_t.config(state='disabled')

showt_t.pack()
showc_t.pack()
w.mainloop()