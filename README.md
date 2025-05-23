# Projekt-Dokumentation

Die vollständige Dokumentation befindet sich unter: `/Writerside`
 docker compose run --remove-orphans automatisierung 20

## Voraussetzungen

- **Python**: Version 3.8 oder höher muss installiert sein.
  - ``sudo apt install python3``
- **PIP**
  - ``sudo apt-get install python3-pip``



## Setup-Anleitung

### 1. Repository klonen
Klonen Sie das Repository auf Ihren lokalen Rechner:

``git clone <repository-url>`` <br>``cd <repository-name>``

### 2. Requirements installieren
``cd setup/``
``pip3 install -r requirements.txt``

### 3. `.env`-Datei konfigurieren
Benennen Sie die Datei `.env.dist` in `.env` um und füllen Sie die erforderlichen Variablen aus, um die Konfiguration anzupassen. Dies erleichtert die Nutzung (Quality of Life).
Die .env befindet sich in Setup

#### Beispiel `.env`-Inhalt:
``DOMAIN=example.com ``- Domainname des Unternehmens<br>
``USERNAME=devops_user ``- DevOps-Benutzername<br>
``PASSWORD=secure_password ``- DevOps-Passwort<br>
``BASEURL=7pace.firma``- Basis-URL (ersetzen Sie 'firma' mit dem tatsächlichen Firmennamen)
``

### 4. Skript ausführen
Starten Sie das Python-Skript mit folgendem Befehl:<br>
``python main.py``

## Hinweise

- Stellen Sie sicher, dass alle Abhängigkeiten installiert sind. Falls nicht, können Sie diese mit `pip install -r requirements.txt` installieren.
- Das Programm funktioniert auch ohne .env
- Bei Problemen oder Fragen konsultieren Sie bitte die vollständige Dokumentation unter `/Writerside`.

---

