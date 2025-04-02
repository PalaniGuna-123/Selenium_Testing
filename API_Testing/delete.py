import requests

api_key = "GjFITtVLtSX3TGT3lhDu"
freshdesk_domain = "ramalakshmilakshmi-assist.freshdesk.com"
ticket_id = 0

url = f"https://{freshdesk_domain}/api/v2/tickets/{ticket_id}"

response = requests.delete(url, auth=(api_key, "X"))

if response.status_code == 204:
    print(f"Ticket {ticket_id} deleted successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
