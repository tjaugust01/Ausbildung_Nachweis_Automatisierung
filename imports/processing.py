from collections import defaultdict
import datetime

def remove_milliseconds(timestamp):
    # Hilfsfunktion - implementieren falls nicht vorhanden
    if '.' in timestamp:
        return timestamp.split('.')[0] + 'Z'
    return timestamp

def sanitize_data(work):
    endTime = datetime.datetime.strptime(remove_milliseconds(work["EditedTimestamp"]), "%Y-%m-%dT%H:%M:%SZ")
    startTime = datetime.datetime.strptime(remove_milliseconds(work["CreatedTimestamp"]), "%Y-%m-%dT%H:%M:%SZ")

    startTime += datetime.timedelta(hours=1)  # Zeitzonenanpassung
    endTime += datetime.timedelta(hours=1)

    weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    weekday = weekdays[startTime.weekday()] if 0 <= startTime.weekday() < 7 else "Unbekannt"
    time = endTime - startTime

    return {
        "weekday": weekday,
        "Comment": work["Comment"],
        "time": time,
        "title": work["WorkItem"]["System_Title"],
        "startTime": startTime,
        "endTime": endTime
    }

def group_by_weekday(work_entries):
    """Gruppiert Arbeitseinträge nach Wochentagen und entfernt das weekday-Feld aus den einzelnen Einträgen"""
    grouped_data = defaultdict(list)
    for entry in work_entries:
        weekday = entry.pop("weekday")  # Entfernt das Feld und gibt den Wert zurück
        grouped_data[weekday].append(entry)
    return dict(grouped_data)
