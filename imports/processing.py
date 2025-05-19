import locale
from collections import defaultdict
import datetime

# Deine bestehenden Funktionen remove_milliseconds und sanitize_data bleiben unverändert
def remove_milliseconds(timestamp_str):
    if "." in timestamp_str:
        return timestamp_str.split(".")[0] + "Z"
    return timestamp_str

def sanitize_data(work):
    startTime = datetime.datetime.strptime(remove_milliseconds(work["Timestamp"]), "%Y-%m-%dT%H:%M:%SZ")
    endTime = startTime + datetime.timedelta(seconds=work["PeriodLength"])
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    return {
        "weekday": startTime.strftime("%A"),
        "details": {
            "startTime": startTime,
            "endTime": endTime,
            "duration": work["PeriodLength"],
            "title": work["WorkItem"]["System_Title"],
            "comment": work["Comment"]
        }
    }

def transform_work_data(works):
    result = {}

    for work in works:
        weekday = work["weekday"]
        details = work["details"]

        startTime = details["startTime"]
        endTime = details["endTime"]
        work_element = {"title": details["title"], "duration": details["duration"]}

        entry = result.get(weekday)
        if entry is None:
            # Erster Eintrag für diesen Wochentag: Initialisieren
            result[weekday] = {
                "start": startTime,
                "end": endTime,
                "elemente": [work_element.copy()]
            }
        else:
            # vorhandenen Zeitraum anpassen
            if startTime < entry["start"]:
                entry["start"] = startTime
            if endTime > entry["end"]:
                entry["end"] = endTime

            # work_element zusammenfassen oder neu hinzufügen
            for elem in entry["elemente"]:
                if elem["title"] == work_element["title"]:
                    elem["duration"] += work_element["duration"]
                    break
            else:
                entry["elemente"].append(work_element.copy())

    return result
