import pandas as pd
import datetime



df = pd.read_excel("Birthday.xlsx")
today = datetime.datetime.now().strftime("%d-%m")

for index, item in df.iterrows():
    bday = item['Date of Birth'].strftime("%d-%m")
    if (today == bday):
        print(item['Date of Birth'],item['Name'])