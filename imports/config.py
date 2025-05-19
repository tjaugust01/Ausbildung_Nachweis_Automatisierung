import os
import getpass
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../setup/.env')
load_dotenv(dotenv_path)

def get_credentials(kw):
    baseurl = os.getenv("BASEURL")
    domain = os.getenv("DOMAIN")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    fullname = os.getenv("FULLNAME")

    return {
        "kw": kw,
        "baseurl": baseurl,
        "domain": domain,
        "username": username,
        "password": password,
        "fullname": fullname
    }
