from imports.config import get_credentials
from imports.api import api_call
from imports.processing import sanitize_data
from imports.pdf import create_worklog_pdf

if __name__ == "__main__":
    credentials = get_credentials()
    data = api_call(credentials)

    if data:
        works = [sanitize_data(work) for work in data["value"]]
        create_worklog_pdf(works, output_pdf="Ausbildungsnachweis.pdf")
