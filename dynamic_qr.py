from auth import headers
import requests

def initiate_dynamic_qr():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/qrcode/v1/generate"
    json = {
        "MerchantName": "TEST",
        "RefNo": "Invoice Test",
        "Amount": 1,
        "TrxCode": "PB",
        "CPI": "174379",
        "Size": "300"
    }
    response = requests.post(api_url, json=json, headers=headers)
    return response.json()

print(initiate_dynamic_qr())