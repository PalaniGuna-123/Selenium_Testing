import requests
import json

api_key = "GjFITtVLtSX3TGT3lhDu"

freshdesk_domain = "ramalakshmilakshmi-assist.freshdesk.com"


url = f"https://{freshdesk_domain}/api/v2/tickets"


headers = {
    "Content-Type": "application/json"
}


data = {
    "subject": "API Testing Ticket",
    "description": "This ticket is created via API request.",
    "email": "user@example.com",
    "priority": 2,
    "status": 1
}

response = requests.post(url, auth=(api_key, "X"), headers=headers, data=json.dumps(data))


if response.status_code == 201:
    print("Ticket Created Successfully!")
    print(response.json())
else:
    print("error",response.json())
