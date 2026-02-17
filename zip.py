x=[1,2,3]
y=[4,5,6]
z=zip(x,y)
print(list(z))
x1,y1=zip(*zip(x,y))
import csv
import pandas as pd
sheet1={"name":[],"age":[]}
sheet1=pd.DataFrame(sheet1)
sheet1.to_csv("grades.csv",index=False)

import csv
import pandas as pd
sheet1={"name":[],"age":[]}
sheet1=pd.DataFrame(sheet1)
sheet1.to_csv("grades.csv",index=False)
print("hi")