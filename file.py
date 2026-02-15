x=open("zainab","w")
x.write("hello world")
x.close()

x=open("zainab","r")
print(x.read())
x.close()

a=open("data","w")
a.write("python is fun and easy")
a.close()
a=open("data","r")
print(a.tell())
print(a.read(6))
print(a.tell())
a.seek(0,0)
print(a.tell())
a.close()
import os
