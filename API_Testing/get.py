import requests
api_key="GjFITtVLtSX3TGT3lhDu"
ticket_id=2
url=f"https://ramalakshmilakshmi-assist.freshdesk.com/api/v2/tickets/{ticket_id}"
response = requests.get(url,auth=(api_key,"X"))
if response.status_code == 200:
        print(response.json())
else:
        print("invalid data")
