import csv
import pandas as pd
sheet1={"name":[],"age":[]}
sheet1=pd.DataFrame(sheet1)
sheet1.to_csv("grades.csv",index=False)

