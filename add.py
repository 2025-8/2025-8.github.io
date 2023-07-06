from tkinter import *

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

w=Tk()
w.geometry('300x300')

w.mainloop()