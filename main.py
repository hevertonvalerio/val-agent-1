import requests
import os
import uuid

APLICATION_TOKEN = os.environ.get("APP_TOKEN")
url = "https://langflow.inovai.app/api/v1/run/61a17804-9284-446d-8e60-3801aef9bb60"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!"
}
payload["session_id"] = str(uuid.uuid4())

headers = {"x-api-key": APLICATION_TOKEN}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")