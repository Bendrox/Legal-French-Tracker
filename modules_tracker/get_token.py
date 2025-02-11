import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()


client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

if not client_id or not client_secret:
    print("Debug : client_id ou client_secret manquant(s) !")
    sys.exit(1)


def get_token():
    token_url = 'https://sandbox-oauth.piste.gouv.fr/api/oauth/token'
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv("client_id") ,
        'client_secret': os.getenv("client_secret"),
        'scope': 'openid'
    }
    response = requests.post(token_url, data=token_data)
    print(f"DEBUG - Status Code: {response.status_code}")
    response.raise_for_status() 
    token_info = response.json()
    access_token = token_info['access_token']
    return access_token

def get_token_prod():
    token_url = 'https://oauth.piste.gouv.fr/api/oauth/token'  # URL  production
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv("client_id_pro"),
        'client_secret': os.getenv("client_secret_pro"),
        'scope': 'openid'
    }
    response = requests.post(token_url, data=token_data)
    print(f"DEBUG - Status Code: {response.status_code}")
    response.raise_for_status() 
    token_info = response.json()
    access_token = token_info['access_token']
    return access_token