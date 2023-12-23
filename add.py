from tkinter import *
from pickle import dump,load

s1='''<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>微信公众号文章链接</title>
        <style>
            a{
                display: block;
                text-decoration: none;
                background-color: rgba(114, 155, 156, 0.44);
                color: black;
            }
            a:hover{
                background-color: rgba(0, 162, 255, 0.626);
                color: white;
            }
            ul{
                list-style-type: none;
            }
        </style>
    </head>
    <body>
        <ul>'''
s2='''</ul>
    </body>
</html>'''

l=load(open('articles','rb'))

def ok_add():
    l.append('<li><a target="_blank" href="'+in_a.get()+'">'+in_title.get()+'</a></li>')
    rewrite()
    fresh()
    in_title.delete(0,'end')
    in_a.delete(0,'end')

def ok_delete():
    l.pop(articles_listbox.curselection()[0])
    rewrite()
    fresh()
    

def ok_insert():
    articles_listbox.insert(articles_listbox.curselection()[0]-1,'<li><a target="_blank" href="'+in_a.get()+'">'+in_title.get()+'</a></li>')
    l.insert(articles_listbox.curselection()[0]-1,'<li><a target="_blank" href="'+in_a.get()+'">'+in_title.get()+'</a></li>')
    rewrite()
    fresh()
    in_title.delete(0,'end')
    in_a.delete(0,'end')

def rewrite():
    dump(l,open('articles','wb'))
    open('wechat_articles.html','w',encoding='utf8').write(s1+'\n'+'\n'.join(l)+s2)

def fresh():
    articles_listbox.delete(0,'end')
    for i in l:
        articles_listbox.insert('end',i)

w=Tk()
w.geometry('1000x300')

articles_listbox=Listbox(w,width=120)

fresh()

in_a_l=Label(w,text='文章链接')
in_a=Entry(w,width=100)
in_title_l=Label(w,text='文章标题')
in_title=Entry(w,width=100)
buttons=Frame(w)

ok_add_b=Button(buttons,command=ok_add,text='追加')
ok_delete_b=Button(buttons,command=ok_delete,text='删除')
ok_insert_b=Button(buttons,command=ok_insert,text='在前插入')

articles_listbox.grid(row=0,column=1)
in_a_l.grid(row=1,column=0)
in_a.grid(row=1,column=1)
in_title_l.grid(row=2,column=0)
in_title.grid(row=2,column=1)
buttons.grid(row=3,column=1)
ok_add_b.grid(row=0,column=0)
ok_delete_b.grid(row=0,column=1)
ok_insert_b.grid(row=0,column=2)

w.mainloop()
