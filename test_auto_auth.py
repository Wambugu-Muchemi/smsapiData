import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
COOKIE = os.getenv("COOKIE")
URL = os.getenv("URL")
TOKEN2 = os.getenv("TOKEN2")
CLIENT_ID = os.getenv("CLIENT_ID")
USER_AGENT = os.getenv("USER_AGENT")

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
print("Bearer "+acc_token3)




