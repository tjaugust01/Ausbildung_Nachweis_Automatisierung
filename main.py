import requests
import getpass
from datetime import datetime
from requests_ntlm import HttpNtlmAuth
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_pdf(worklog):
    kw = worklog["StartTime"].isocalendar().week
    datum = worklog["StartTime"].strftime("%Y-%m-%d")

    # PDF-Datei und Seite erstellen
    c = canvas.Canvas("a", pagesize=A4)
    width, height = A4


    # Text hinzufügen
    c.drawString(100, height - 100, "Hallo, dies ist ein PDF-Beispiel!")

    # Rechteck zeichnen
    c.rect(100, height - 200, 400, 100, stroke=1, fill=0)

    # Neuen Text in das Rechteck einfügen
    c.drawString(120, height - 220, "Dies ist ein Text in einem Rechteck.")

    # PDF speichern
    c.save()


# PDF erstellen




def remove_milliseconds(timestamp):
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        # Falls keine Millisekunden vorhanden sind, geben Sie den ursprünglichen String zurück
        return timestamp


domain= input("Gib dein Domain ein: ")
username = input("Gib deinen Usernamen ein: ")
# Unsichtbare Eingabe
password = getpass.getpass("Gib dein Passwort ein")
baseurl= input("Gib dein Base URL ein ( https://________.__/ | 7pace.firma) : ")
api_url= "https://" + baseurl + "/api/" + domain + "/odata/v3.2/workLogsWorkItems?$select=EditedTimestamp,CreatedTimestamp,WorkItem,Comment&$filter=(Timestamp%20ge%202025-03-10T00:00:00Z%20and%20Timestamp%20le%202025-03-17T23:59:59Z)"


# Define your NTLM credentials (use domain if required)
domainuser=domain+'\\'+username

# Make an authenticated request
response = requests.get(api_url, auth=HttpNtlmAuth(domainuser, password))

# Print response
if response.status_code == 200:
    print("Authentication successful!")
    data = response.json()
    worklog = {}
    for work in data["value"]:
        comment= work["Comment"] if work["Comment"] else "Kein Kommentar"
        startTime = remove_milliseconds(work["EditedTimestamp"])
        endTime = remove_milliseconds(work["CreatedTimestamp"])
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        startTime = datetime.strptime(startTime, fmt)
        endTime = datetime.strptime(endTime, fmt)
        diff = startTime - endTime
        worklog["StartTime"] = startTime
        worklog["EndTime"] = endTime
        worklog["Comment"] = comment
        worklog["Title"] = work["WorkItem"]["System_Title"]
        worklog["Time"] = diff
        print(worklog["StartTime"])
        print("--------------------------------")
    create_pdf("beispiel.pdf")
else:
    print(f"Failed! Status Code: {response.status_code}, Response: {response.text}")