import requests
import json

url = "https://account.africastalking.com/api/v1/auth/signin"

payload = json.dumps({
  "email": "dmain5054@gmail.com",
  "password": "YDkaft@DVc7fVyH",
  "timeOffset": 720
})
headers = {
  'X-Client-Id': 'nest.account.dashboard',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTY0MjYsImZpcnN0TmFtZSI6IkRhbm5pZSIsImxhc3ROYW1lIjoiTGFicyIsImVtYWlsIjoiZG1haW41MDU0QGdtYWlsLmNvbSIsImNvdW50cnkiOiJLZW55YSIsImN1cnJlbmN5IjoiS0VTIiwidGltZU9mZnNldCI6NzIwLCJhY3RpdmF0ZWQiOnRydWUsInJvbGUiOiJub3JtYWwiLCJpbnRlcmNvbSI6eyJ1c2VyX2hhc2giOiJhMzJkMDg4ODk5YTFmZDYyZDZjNTg0MDA1MzBkMDI1MDI5MzIwNTg3OWI2N2UwNGU4ODA0Zjk1NzFlNDA5ZmQyIn0sInNsYWNrIjpudWxsLCJsb2NhbGUiOiJISyIsImNsaWVudElkIjoibmVzdC5hY2NvdW50LmRhc2hib2FyZCIsImlhdCI6MTYyMzA2ODM4MywiZXhwIjoxNjIzMDcxOTgzLCJpc3MiOiJodHRwczovL2FjY291bnQuYWZyaWNhc3RhbGtpbmcuY29tIiwic3ViIjoiZG1haW41MDU0QGdtYWlsLmNvbSIsImp0aSI6IjYwYmUwZWRmNjU3ZGE2ZDVhMTE2ZDNiMCJ9.RQNeZgcwRhAhl80NvQ1VV_PteGW1dioh53fioeZFn8g',
  'Cookie': 'nalb=http://10.222.105.54:8080'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
