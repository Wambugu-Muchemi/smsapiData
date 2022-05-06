import requests
import json
from dotenv import load_dotenv
import os
import time

while(True):

    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    COOKIE = os.getenv("COOKIE")
    URL = os.getenv("URL")
    TOKEN2 = os.getenv("TOKEN2")
    CLIENT_ID = os.getenv("CLIENT_ID")
    USER_AGENT = os.getenv("USER_AGENT")

    def main():
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


        accesstoken_dict = response.json()['data']


        accesstoken = accesstoken_dict.get('access_token')
        with open('.bear','w') as file:
            file.writelines(f"Bearer {accesstoken}")
            #print(accesstoken)
        file.close()

        return None

    if __name__ == "__main__":
        main()

    time.sleep(300)


