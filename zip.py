x=[1,2,3]
y=[4,5,6]
z=zip(x,y)
print(list(z))
x1,y1=zip(*zip(x,y))
