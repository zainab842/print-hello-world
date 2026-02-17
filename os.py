import os
z=open("zainab","w")
z.write( "hello world")
print(z.tell())
z.close()
z=open("zainab","r")
print(z.read())
print(z.seek(0,0))
print(z.tell())


z.close()
os.remove("zainab")
os.mkdir("zozo")
os.rmdir("zozo")
