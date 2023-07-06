from os import system
from random import randint

system("git add .")
system('git commit -m "'+str(randint(1,1e15))+'"')
system("git push origin")
system("zzh100415\n")