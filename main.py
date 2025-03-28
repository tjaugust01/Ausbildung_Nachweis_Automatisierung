from imports.config import get_credentials
from imports.api import api_call
from imports.processing import sanitize_data, group_by_weekday
import imports.pdf as pdf
from collections import defaultdict

if __name__ == "__main__":
    # 1. Daten abrufen
    credentials = get_credentials()
    api_data = api_call(credentials)

    if not api_data:
        print("Keine Daten erhalten")
        exit()

    # 2. Daten bereinigen und strukturieren
    works = [sanitize_data(work) for work in api_data["value"]]

    # 3. Daten nach Wochentagen gruppieren
    grouped_works=group_by_weekday(works)
    # 4. PDF erstellen
    pdf.create_pdf(grouped_works, credentials["fullname"], credentials["kw"])
