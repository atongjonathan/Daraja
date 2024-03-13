import requests
import base64
from dotenv import load_dotenv
import os
import json

load_dotenv("config.env")


test_1 = json.loads(os.environ.get("test_1"))
test_2 = json.loads(os.environ.get("test_2"))
test_3 = json.loads(os.environ.get("test_3"))
PHONE_NO = os.environ.get("PHONE_NO")

# Getting access token


def get_access_token(credentials: dict):
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    headers = {'Content-Type': 'application/json'}
    auth = (credentials.get("consumer_key"),
            credentials.get("consumer_secret"))
    response = requests.get(access_token_url, headers=headers, auth=auth)
    response.raise_for_status()
    result = response.json()
    access_token = result['access_token']
    return access_token

def bearer_header(credentials:dict):
    access_token = get_access_token(credentials)
    headers = {
    "Authorization": f"Bearer " + access_token,
    'Content-Type': 'application/json'}
    return headers


def get_headers(credentials:dict):
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + get_access_token(credentials),
    "X-appKey": credentials.get("consumer_key")
}
    return headers

headers = get_headers(test_3)




