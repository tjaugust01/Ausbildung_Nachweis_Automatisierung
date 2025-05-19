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
    return {
        "weekday": startTime.strftime("%A"), # Stellt sicher, dass der Wochentag korrekt generiert wird
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
        weekday = work["weekday"].lower()
        details = work["details"]

        startTime = details["startTime"]
        endTime = details["endTime"]

        work_element = {"title": details["title"], "duration": details["duration"]}

        if weekday not in result:
            result[weekday] = {
                "start": startTime,
                "end": endTime,
                "elemente": [work_element]
            }
        else:
            if startTime < result[weekday]["start"]:
                result[weekday]["start"] = startTime
            if endTime > result[weekday]["end"]:
                result[weekday]["end"] = endTime
            result[weekday]["elemente"].append(work_element)

    return result