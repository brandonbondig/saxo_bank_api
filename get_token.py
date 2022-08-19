import time
import requests
from urllib.parse import urlencode
from playwright.sync_api import sync_playwright
import json
import datetime

f = open("userInfo.json")
userInfo = json.load(f)



REDIRECT_URI = "http://localhost:3000/callback/api"

class OAUTH2:
    def __init__(self, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):

        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.REDIRECT_URI = REDIRECT_URI

        if len(CLIENT_ID) < 31 or CLIENT_ID == "CLIENT_ID":
            print("Error: is userInfo.json filled correctly?")
            quit()
        if len(CLIENT_SECRET) < 31 or CLIENT_SECRET == "CLIENT_SECRET":
            print("Error: is userInfo.json filled correctly?")
            quit()

    def saxobank(self):

        params = {"client_id": self.CLIENT_ID, "redirect_uri": self.REDIRECT_URI}
        endpoint = "https://live.logonvalidation.net/authorize"
        endpoint = f"{endpoint}?response_type=code&{urlencode(params)}"

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(endpoint, timeout=0)
            page.wait_for_selector("body > pre")
            code = json.loads(page.inner_text("body"))
            code = code["code"]

        params = {
            "client_id": self.CLIENT_ID,
            "grant_type": "authorization_code",
            "client_secret": self.CLIENT_SECRET,
            "redirect_uri": self.REDIRECT_URI,
            "code": code,
        }

        endpoint = "https://live.logonvalidation.net/token"

        response = requests.post(
            endpoint, params=params, headers={"Accept": "application/json"}
        ).json()

        json_object = json.dumps(response, indent=4)
 
        # Writing to sample.json
        with open("token.json", "w") as outfile:
            outfile.write(json_object)

        # Refresh Access Token
        print("Auto Refresh Token Running")

        while True:
            
            time.sleep(1000)
            
            f = open("token.json")
            data = json.load(f)

            params = {
            "client_id": self.CLIENT_ID,
            "grant_type": "refresh_token",
            "client_secret": self.CLIENT_SECRET,
            "refresh_token": data['refresh_token'],
            }

            endpoint = "https://live.logonvalidation.net/token"

            response = requests.post(endpoint, params=params, headers={"Accept": "application/json"}).json()

            json_object = json.dumps(response, indent=4)
    
            # Writing to sample.json
            with open("response.json", "w") as outfile:
                outfile.write(json_object)
            print(f"{datetime.datetime.now()} - token refreshed")


OAUTH2(userInfo['CLIENT_ID'], userInfo['CLIENT_SECRET'], REDIRECT_URI).saxobank()

