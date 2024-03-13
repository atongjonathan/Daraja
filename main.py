import requests
from auth import headers
# Onboarding Generic API


def onboarding():
    """
        This is the first API used to opt you as a biller to our bill manager features. Once you integrate to this API and send a request with a success response, your shortcode is whitelisted and you are able to integrate with all the other remaining bill manager APIs.

        Returns:
            dict:
                "app_key":"AG_2376487236_126732989KJ",
                "resmsg":"Success",
                "rescode":"200"
    """

    request_body = {
        "shortcode": 174379,
        "email": "atongjonathan@gmail.com",
        "officialContact": "0708683896",
        "sendReminders": "1",
        "logo": "image",
        "callbackurl": "http://my.server.com/bar/callback"
    }

    api_url = "https://api.safaricom.co.ke/v1/billmanager-invoice/optin"
    response = requests.post(url=api_url, headers=headers, json=request_body)
    return response.json()


# Single Invoicing - Generic API

def single_invoicing():
    api_url = "https://api.safaricom.co.ke/v1/billmanager-invoice/single-invoicing"
    request_body = {
  "externalReference": "19315442561",
  "billedFullName": "John Doe",
  "billedPhoneNumber": "254726304245",
  "billedPeriod": "August 2021",
  "invoiceName": "Invoice Test",
  "dueDate": "2021-09-15 00:00:00.00",
  "accountReference": "Balboa45",
  "amount": "2000",
  "invoiceItems": [
        {
            "itemName": "food",
            "amount": "1000"
        },
        {
            "itemName": "water",
            "amount": "1000"
        },
    ]
}
    response = requests.post(url=api_url, headers=headers, json=request_body)

    return response.json()

# print(onboarding())

def update_opt_in():
    api_url = "https://sandbox.safaricom.co.ke/v1/billmanager-invoice/change-optin-details"
    json = {
  "officialContact": "0708683896",
  "email": "atongjonathan@gmail.com"
}
    response = requests.post(api_url, json=json, headers=headers)
    return response.json()
print(single_invoicing())
