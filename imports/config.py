import os
import getpass
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../setup/.env')
load_dotenv(dotenv_path)

def get_credentials():
    baseurl = os.getenv("BASEURL") or input("Gib dein API URL ein: ")
    domain = os.getenv("DOMAIN") or input("Gib deine Domain ein: ")
    username = os.getenv("USERNAME") or input("Gib deinen Usernamen ein: ")
    password = os.getenv("PASSWORD") or getpass.getpass("Gib dein Passwort ein: ")
    fullname = os.getenv("FULLNAME") or input("Dein Vollständiger Name")
    kw = int(input("Gib die gewünschte KW an (z. B.: 11): "))

    return {
        "kw": kw,
        "baseurl": baseurl,
        "domain": domain,
        "username": username,
        "password": password,
        "fullname": fullname
    }
