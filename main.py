import requests
import getpass
from datetime import datetime

import json
from requests_ntlm import HttpNtlmAuth


domain= input("Gib dein Domain ein: ")
username = input("Gib deinen Usernamen ein: ")
# Unsichtbare Eingabe
password = getpass.getpass("Gib dein Passwort ein: ")




# Define API URL

# Define your NTLM credentials (use domain if required)
domainuser=domain+'\\'+username

# Make an authenticated request
response = requests.get(api_url, auth=HttpNtlmAuth(domainuser, password))

# Print response
if response.status_code == 200:
    print("Authentication successful!")
    data = response.json()
    for work in data["value"]:
        comment= work["Comment"] if work["Comment"] else "Kein Kommentar"
        startTime = work["EditedTimestamp"][:-1]  # Entfernt das 'Z'
        startTime = startTime[:26] + 'Z'  # Kürzt auf 6 Millisekunden

        endTime = work["CreatedTimestamp"][:-1]
        endTime = endTime[:26] + 'Z'
        fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
        dt1 = datetime.strptime(startTime, fmt)
        dt2 = datetime.strptime(endTime, fmt)
        # time=endTime-startTime
        time=dt2-dt1
        print (dt2)
        print(dt1)
        print(work["EditedTimestamp"])
        print(work["CreatedTimestamp"])
        print(work["WorkItem"]["System_Title"])
        print("--------------------------------")
else:
    print(f"Failed! Status Code: {response.status_code}, Response: {response.text}")
