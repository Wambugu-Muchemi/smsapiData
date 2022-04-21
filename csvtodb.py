from asyncore import write
from csv import writer
import csv
import requests
import subprocess
from unicodedata import name
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

url = "https://account.africastalking.com/api/v1/apps/jndydujron/sms/bulk/outbox?page=0&count=100"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTY0MjYsImZpcnN0TmFtZSI6IkRhbm5pZSIsImxhc3ROYW1lIjoiTGFicyIsImVtYWlsIjoiZG1haW41MDU0QGdtYWlsLmNvbSIsImNvdW50cnkiOiJLZW55YSIsImN1cnJlbmN5IjoiS0VTIiwidGltZU9mZnNldCI6NzIwLCJhY3RpdmF0ZWQiOnRydWUsInJvbGUiOiJub3JtYWwiLCJpbnRlcmNvbSI6eyJ1c2VyX2hhc2giOiJhMzJkMDg4ODk5YTFmZDYyZDZjNTg0MDA1MzBkMDI1MDI5MzIwNTg3OWI2N2UwNGU4ODA0Zjk1NzFlNDA5ZmQyIn0sInNsYWNrIjpudWxsLCJsb2NhbGUiOiJISyIsImNsaWVudElkIjoibmVzdC5hY2NvdW50LmRhc2hib2FyZCIsImlhdCI6MTY1MDUyMTYzMSwiZXhwIjoxNjUwNTI1MjMxLCJpc3MiOiJodHRwczovL2FjY291bnQuYWZyaWNhc3RhbGtpbmcuY29tIiwic3ViIjoiZG1haW41MDU0QGdtYWlsLmNvbSIsImp0aSI6IjYyNjBmNjFlOTg3ZTE3OTBmMDExZjIwZSJ9.4mg81S8k8OiByHQYEQpoKQeiONl0J4G5cVz0ILM2Y4M',
  'X-Client-Id': 'nest.account.dashboard',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'Accept': '*/*',
  'Cookie': 'nalb=http://10.222.105.54:8080'
}


response = requests.request("GET", url, headers=headers, data=payload)

#Test if token still active
if response.status_code == 200:
    print('API call successful.')
elif response.status_code == 401:
    print('API call failed. Check Token.')
else:
    print('Token still active but something else happened. Attention required!')

#Store the json data in a variable
myjson = response.json()
ourdata =[]
#create the csv column headers
csvheader = ['created','message','recipient','status']

#listing data to source from json
for x in myjson['data']:
    listing = [x['created'],x['message'],x['recipient'],x['status']]
   
    ourdata.append(listing)

#write to csv
with open('smscode.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)
print('Done! CSV file ready to be updated to DB.')

#import updated csv to db
engine = create_engine("postgresql+psycopg2://postgres:muchemi@localhost:5432/smscodedb")
csvfile= '/home/wambugumuchemi/smsapicode/smscode.csv'
df = pd.read_csv(csvfile)
try:
    df.to_sql('sms_data',engine,if_exists='append',index=False)
finally:
    engine.dispose()

print('DB successfully updated.')   

