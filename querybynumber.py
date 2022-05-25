import requests
import json
import os

phone = input("Enter Number(e.g 701888666)")
cleanedphone = f"%2B254{phone}"
f"{cleanedphone}"
with open('.bear', 'r') as f:
    accesstoken = f.read()
url = f"https://account.africastalking.com/api/v1/apps/jndydujron/sms/bulk/outbox?filter=recipient&value={cleanedphone}&page=0&count=1"

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
if response.status_code == 401:
    print('API token issue encountered.')
else: print("...")
#print(response.text)
message_dict = response.json()['data']
code =message_dict[0]['message'][0:4]
if int(code):
    print(code)
else:
    print('Err')
try:{
    int(code)
    
}
except:{
    print('No code found. Recheck if this number is registered with us or try requesting another.')

}

""" if message_dict == []:
    print('No message history found. Recheck if this number is registered with us.')
else:
    message1 = message_dict[0]['message']
    message2 = message_dict[1]['message']
    message3 = message_dict[2]['message']
    message4 = message_dict[3]['message']
    message5 = message_dict[4]['message']
    message6 = message_dict[5]['message']
    message7 = message_dict[6]['message']
    message8 = message_dict[7]['message']
    message9 = message_dict[8]['message']
    message10 = message_dict[9]['message']

    # print('\n1. '+message1)
    # print('\n2. '+message2)
    # print('\n3. '+message3)
    selection = input('Enter 1 for Sub ID or 2 for SMS code:')
    #print(selection)
    if (selection == '1'):
        if 'subscription' in message1:
            print(message1)
        elif 'subscription' in message2:
            print(message2)
        elif 'subscription' in message3:
            print(message3)
        elif 'subscription' in message4:
            print(message4)
        elif 'subscription' in message5:
            print(message5)
        elif 'subscription' in message6:
            print(message6)
        elif 'subscription' in message7:
            print(message7)  
        elif 'subscription' in message8:
            print(message8)
        elif 'subscription' in message9:
            print(message9)     
        elif 'subscription' in message10:
            print(message10)             
        else:
            print('No Sub ID message found. Please recheck number or reach out to your regional technical support for help.')          
    elif (selection == '2'):
        if 'verification' in message1:
            print(message1)
        elif 'verification' in message2:
            print(message2)
        elif 'verification' in message3:
            print(message3)
        elif 'verification' in message4:
            print(message4)
        elif 'verification' in message5:
            print(message5)
        elif 'verification' in message6:
            print(message6)
        elif 'verification' in message7:
            print(message7)  
        elif 'verification' in message8:
            print(message8)
        elif 'verification' in message9:
            print(message9)     
        elif 'verification' in message10:
            print(message10)    
        else:
            print('No SMS code message found. Please recheck number or reach out to your regional technical support for help.')
    else:
        print('Unknown selection.')
 """