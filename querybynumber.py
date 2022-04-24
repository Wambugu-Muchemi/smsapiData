import requests
import json
import os

phone = input("Enter #(711759446)")
cleanedphone = f"%2B254{phone}"
f"{cleanedphone}"
with open('.bear', 'r') as f:
    accesstoken = f.read()
url = f"https://account.africastalking.com/api/v1/apps/jndydujron/sms/bulk/outbox?filter=recipient&value={cleanedphone}&page=0&count=3"

payload='from=1-1-2022'
headers = {
  'Authorization': accesstoken,
  'X-Client-Id': 'nest.account.dashboard',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'Accept': '*/*',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'nalb=http://10.222.233.44:8080'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
message_dict = response.json()['data']
message = message_dict[0]['message']
print(message)
