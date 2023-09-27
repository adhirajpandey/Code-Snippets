import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# webhook url
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# message to be sent
test_message = "Hello, World! This is a webhook test!"

# headers
headers = {
    "Content-Type": "application/json"
}

# data to be sent to discord
data = {
    "content": test_message,
    "username": "My Interesting Webhook Name",
    # "avatar_url": "https://i.imgur.com/4M34hi2.png"  # uncomment , remove , replace as needed
}

# sending post request and saving response as response object
response_data = requests.post(url=webhook_url, data=json.dumps(data), headers=headers)

print("Message Sent Successfully!")
print("Response: " + str(response_data.status_code) + " " + response_data.reason)