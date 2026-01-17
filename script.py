#!/bin/python3


import requests
import hmac
import hashlib
from datetime import datetime, timezone


timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
timestamp = timestamp.replace("+00:00", "Z")


payload = {
    "timestamp": timestamp,
    "name": "Magnus Tetteh",
    "email": "tettehmagnus35@gmail.com",
    "resume_link": "https://drive.google.com/file/d/1frq0j4KrX6jKUZJcntrsUCBPn_FhwUGi/view?usp=sharing"
    # "repository_link":
    # "action_run_link":
}


headers = {
    "X-Signature-256": ""
}

response = requests.post(
    url="https://b12.io/apply/submission",

)





