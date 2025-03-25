import datetime


def remove_milliseconds(timestamp):
    return timestamp.split('.')[0] + 'Z' if '.' in timestamp else timestamp


def sanitize_data(work):
    endTime = datetime.datetime.strptime(remove_milliseconds(work["EditedTimestamp"]), "%Y-%m-%dT%H:%M:%SZ")
    startTime = datetime.datetime.strptime(remove_milliseconds(work["CreatedTimestamp"]), "%Y-%m-%dT%H:%M:%SZ")

    startTime += datetime.timedelta(hours=1)
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
