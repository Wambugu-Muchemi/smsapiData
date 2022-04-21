from asyncore import write
from csv import writer
import csv
import requests
import subprocess
from unicodedata import name
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os
import json
#

load_dotenv()
URL2 = os.getenv("URL2")
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
USER_AGENT = os.getenv("USER_AGENT")
COOKIE2 = os.getenv("COOKIE2")
API_KEY = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
COOKIE = os.getenv("COOKIE")
URL = os.getenv("URL")
TOKEN2 = os.getenv("TOKEN2")

url = URL

payload = json.dumps({
  "email": EMAIL,
  "password": PASSWORD,
  "timeOffset": 720
})
headers = {
  'X-Client-Id': CLIENT_ID,
  'User-Agent': USER_AGENT,
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Authorization': TOKEN2,
  'Cookie': COOKIE
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)

acc_token = json.loads(response.text)
acc_token2 = acc_token['data']
acc_token3 = acc_token2['access_token']
acc_token4 = "Bearer "+acc_token3

url = URL2

payload={}
headers = {
  'Authorization': acc_token4,
  'X-Client-Id': CLIENT_ID,
  'User-Agent': USER_AGENT,
  'Accept': '*/*',
  'Cookie': COOKIE2
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
#print(myjson)
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

