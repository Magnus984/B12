#!/bin/python3.13

import requests
import hmac
import hashlib
import json
from datetime import datetime, timezone
from dotenv import load_dotenv
from os import getenv


load_dotenv()

timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
timestamp = timestamp.replace("+00:00", "Z") 


payload = {
    "action_run_link": getenv("ACTION_RUN_LINK"),
    "email": "tettehmagnus35@gmail.com",
    "name": "Magnus Tetteh",
    "repository_link": "https://github.com/Magnus984/B12",
    "resume_link": "https://drive.google.com/file/d/1frq0j4KrX6jKUZJcntrsUCBPn_FhwUGi/view?usp=sharing",
    "timestamp": timestamp,
}

# Create compact JSON with sorted keys
payload_json = json.dumps(payload, separators=(',', ':'))

secret = getenv("SECRET")
if not secret:
    raise ValueError("Secret not found")
print("Secret loaded successfully")

digest = hmac.new(
    key=bytes(secret, "utf-8"),
    msg=payload_json.encode('utf-8'),
    digestmod=hashlib.sha256
).hexdigest()


headers = {
    "X-Signature-256": f"sha256{digest}"
}

response = requests.post(
    url="https://b12.io/apply/submission",
    headers=headers,
    json=payload

)

if (response.status_code != 200):
    response.raise_for_status()

print(response.text)




