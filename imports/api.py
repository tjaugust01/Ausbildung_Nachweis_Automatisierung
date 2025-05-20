import datetime
import requests
from requests_ntlm import HttpNtlmAuth

def api_call(api_data):
    kw = api_data["kw"]
    current_year = datetime.datetime.now().year
    montag = str(datetime.date.fromisocalendar(current_year, int(kw), 1))
    sonntag = str(datetime.date.fromisocalendar(current_year, int(kw), 7))

    api_url = (
        f"https://{api_data['baseurl']}/api/{api_data['domain']}/odata/v3.2/"
        f"workLogsWorkItems?$select=Timestamp,PeriodLength,WorkItem,Comment&"
        f"$filter=(Timestamp ge {montag}T00:00:00Z and Timestamp le {sonntag}T23:59:59Z)"
    )

    domainuser = f"{api_data['domain']}\\{api_data['username']}"
    response = requests.get(api_url, auth=HttpNtlmAuth(domainuser, api_data["password"]))

    if response.status_code == 200:
        return response.json()
    else:
        print("Authentication failed. Status code:", response.status_code)
        return None
