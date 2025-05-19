import sys

from imports.config import get_credentials
from imports.api import api_call
from imports.processing import sanitize_data, transform_work_data
import imports.pdf as pdf

if __name__ == "__main__":

    if len(sys.argv) > 1:
        credentials = get_credentials(sys.argv[1])
    else:
        exit("Keine Parameter angegeben.")
    api_data = api_call(credentials)

    if not api_data:
        print("Keine Daten erhalten")
        exit()

    # 2. Daten bereinigen und strukturieren
    works = [sanitize_data(work) for work in api_data["value"]]
    test= transform_work_data(works)
    # print(test)
    pdf.create_pdf(test,credentials["kw"], credentials["fullname"] )
