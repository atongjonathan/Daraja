import requests
from datetime import datetime
import base64
from auth import headers, PHONE_NO
import base64


def initiate_stk_push():
    amount = 1
    phone = PHONE_NO
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    business_short_code = '174379'
    process_request_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    callback_url = 'https://atongjona2.pythonanywhere.com/'
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        (business_short_code + passkey + timestamp).encode()).decode()
    party_a = phone
    account_reference = "Parent's Portal"
    transaction_desc = "Test"

    json = {
        'BusinessShortCode': business_short_code,
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': amount,
        'PartyA': party_a,
        'PartyB': business_short_code,
        'PhoneNumber': party_a,
        'CallBackURL': callback_url,
        'AccountReference': account_reference,
        'TransactionDesc': transaction_desc
    }

    response = requests.post(process_request_url, headers=headers, json=json)
    response_data = response.json()
    return response_data


def query_status(requestID):
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    business_short_code = '174379'
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode(
        (business_short_code + passkey + timestamp).encode()).decode()
    json = {
        "BusinessShortCode": "174379",
        "Password": password,
        "Timestamp": timestamp,
        "CheckoutRequestID": requestID,
    }
    response = requests.post(api_url, json=json, headers=headers)
    return response.json()


print(initiate_stk_push())
# print(query_status("ws_CO_12032024091213124708683896"))
