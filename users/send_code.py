import json

import requests
from django.conf import settings


def get_token():
    url = "https://notify.eskiz.uz/api/auth/login"
    payload = {
        'email': settings.SMS_EMAIL,
        'password': settings.SMS_KEY
    }

    response = requests.request("POST", url, headers={}, data=payload, files=[])
    if response.status_code == 200:
        return json.loads(response.text)["data"].get("token")


def send_code_to_phone(phone: str, code):
    url = "https://notify.eskiz.uz/api/message/sms/send"

    payload = {
        'mobile_phone': phone.strip("+"),
        'message': f'Your verification code: {code}',
        'from': '4546',
        'callback_url': 'http://0000.uz/test.php'
    }
    headers = {
        "Authorization": f"Bearer {get_token()}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)
