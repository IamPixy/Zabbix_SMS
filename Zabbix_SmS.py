#!/usr/bin/python3
# Python samples are made with Requests: HTTP for Humans

import requests

url = "https://sms.magfa.com/api/http/sms/v2/send"
headers = {'accept': "application/json", 'cache-control': "no-cache"}

# Credentials
username = "your UserName"
password = "Your Password"
domain = "Your Domain"
magfaNumber = "Your Magfa Number"
text = 'Put the Message that you want to send here'
receivers = ['Number 1', 'Number 2']



payload_json = {'senders': magfaNumber, 
                'messages':text, 
                'recipients': receivers}

# Call json
response = requests.post(url, headers=headers, auth=(username + '/' + domain, password), json=payload_json)
