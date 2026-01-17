#!/bin/python3.13


import requests
import hmac
import hashlib
from datetime import datetime, timezone
from dotenv import load_dotenv
from os import getenv


load_dotenv()

timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
timestamp = timestamp.replace("+00:00", "Z") 


payload = {
    "timestamp": timestamp,
    "name": "Magnus Tetteh",
    "email": "tettehmagnus35@gmail.com",
    "resume_link": "https://drive.google.com/file/d/1frq0j4KrX6jKUZJcntrsUCBPn_FhwUGi/view?usp=sharing",
    "repository_link": "https://github.com/Magnus984/B12",
    # "action_run_link":
    "linkedin_profile": "www.linkedin.com/in/magnus-tetteh-b1b208213"
}

digest = hmac.new(
    key=bytes(getenv("SECRET"), "utf-8"),
    msg=bytes(str(payload), "utf-8"),
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




