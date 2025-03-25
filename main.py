from calendar import weekday

import requests
import getpass
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from requests_ntlm import HttpNtlmAuth
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
load_dotenv()

def create_worklog_pdf(works, output_pdf="worklogs.pdf"):
    """
    Erstelle eine PDF, in der für jeden Wochentag die zugehörigen Worklogs gelistet werden.
    """

    # Reihenfolge der Wochentage, wie sie in deiner sanitize_data-Funktion vorkommen könnten
    weekdays_order = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    # PDF vorbereiten
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setTitle("Worklogs nach Wochentag")

    # Schrift einstellen
    c.setFont("Helvetica", 12)

    # Startposition für den Text
    x_margin = 50
    y_position = 800  # etwas unterhalb des Seitenrandes

    # Für jeden Tag einen Abschnitt
    for day in weekdays_order:
        # Überschrift für den Tag
        c.drawString(x_margin, y_position, f"{day}:")
        y_position -= 20  # etwas Platz runter

        # Alle Worklogs des aktuellen Tages
        day_worklogs = [wl for wl in works if wl["weekday"] == day]
        if not day_worklogs:
            # Falls es keine Einträge für diesen Tag gibt, kurz vermerken
            c.drawString(x_margin + 10, y_position, "Keine Einträge")
            y_position -= 40  # und weiter runter
        else:
            # Worklogs ausgeben
            for wl in day_worklogs:
                # Beispielhafte Ausgabe: Zeiten, Titel und Kommentar
                start_str = wl["startTime"].strftime("%Y-%m-%d %H:%M")
                end_str = wl["endTime"].strftime("%Y-%m-%d %H:%M")
                title = wl["title"]
                comment = wl["Comment"]
                duration_str = str(wl["time"])  # z.B. "0:30:00" für 30 Minuten

                line_text = f"{start_str} - {end_str} ({duration_str})"
                c.drawString(x_margin + 10, y_position, line_text)
                y_position -= 20

                line_text = f"{title} | {comment}"
                c.drawString(x_margin + 10, y_position, line_text)
                y_position -= 40
                # Seitenumbruch, falls wir zu tief kommen
                if y_position < 50:
                    c.showPage()  # Seite abschließen
                    c.setFont("Helvetica", 12)  # Schrift neu setzen
                    y_position = 800  # Zurück zum oberen Rand

            # Nach den Einträgen für diesen Tag etwas Platz lassen
            y_position -= 20

        # Falls wir wieder unten ankommen, ebenfalls Seitenumbruch
        if y_position < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = 800


    # Abschließen und PDF speichern
    c.showPage()
    c.save()
    print(f"PDF wurde erstellt: {output_pdf}")
def get_credentials():
    import os
    import getpass

    if os.getenv("BASEURL"):
        baseurl = os.getenv("BASEURL")
    else:
        baseurl = input("Gib dein API URL ein (https://________.__/ | 7pace.firma): ")

    if os.getenv("DOMAIN"):
        domain = os.getenv("DOMAIN")
    else:
        domain = input("Gib dein Domain ein: ")

    if os.getenv("USERNAME"):
        username = os.getenv("USERNAME")
    else:
        username = input("Gib deinen Usernamen ein: ")

    if os.getenv("PASSWORD"):
        password = os.getenv("PASSWORD")
    else:
        password = getpass.getpass("Gib dein Passwort ein: ")
    kw=input("Gib die Gewünschte KW an (bswp.:11)")
    return {
        "kw":kw,
        "baseurl": baseurl,
        "domain": domain,
        "username": username,
        "password": password
    }



def api_call(api_data):
    kw=api_data["kw"]
    montag="2025-01-01"
    sonntag="2025-01-01"
    api_url= "https://" + api_data["baseurl"] + "/api/" + api_data["domain"] + "/odata/v3.2/workLogsWorkItems?$select=EditedTimestamp,CreatedTimestamp,WorkItem,Comment&$filter=(Timestamp%20ge%20"+montag+"T00:00:00Z%20and%20Timestamp%20le%20"+sonntag+"T23:59:59Z)"

    # Define your NTLM credentials (use domain if required)
    domainuser=api_data["domain"]+'\\'+ api_data["username"]
    print(api_url)
    # Make an authenticated request
    response = requests.get(api_url, auth=HttpNtlmAuth(domainuser, api_data["password"]))

    if response.status_code == 200:
        json_data = response.json()
        print("Authentication successful!")
        return json_data
    else:
        print("Authentication failed. Status code:", response.status_code)
        return None

def remove_milliseconds(timestamp):
    if '.' in timestamp:
        return timestamp.split('.')[0] + 'Z'
    else:
        return timestamp

def sanitize_data (work):
    endTime = datetime.strptime(remove_milliseconds(work["EditedTimestamp"]),format("%Y-%m-%dT%H:%M:%SZ"))
    startTime = datetime.strptime(remove_milliseconds(work["CreatedTimestamp"]),format("%Y-%m-%dT%H:%M:%SZ"))
    startTime = startTime + timedelta(hours=1)
    endTime = endTime + timedelta(hours=1)
    wochen_index=startTime.weekday()
    match wochen_index:
        case 0:
            weekday="Montag"
        case 1:
            weekday="Dienstag"
        case 2:
            weekday="Mittwoch"
        case 3:
            weekday="Donnerstag"
        case 4:
            weekday="Freitag"
        case 5:
            weekday="Samstag"
        case 6:
            weekday="Sonntag"
        case _:
            weekday="Unbekannt"
    time = endTime - startTime

    workdata={}
    workdata["weekday"]=weekday
    workdata["Comment"]=work["Comment"] if work["Comment"] else "Kein Kommentar"
    workdata["time"]=time
    workdata["title"]=work["WorkItem"]["System_Title"]
    workdata["startTime"]=startTime
    workdata["endTime"]=endTime
    return workdata

if __name__ == "__main__":
    credentials = get_credentials()
    data = api_call(credentials)
    works=[]
    for work in data["value"]:
        worklog=sanitize_data(work)
        print(worklog)
        works.append(worklog)

create_worklog_pdf(works, output_pdf="meine_worklogs.pdf")

