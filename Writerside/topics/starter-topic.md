# 1. Einführung und Ziele

## Was ist das Projekt

Das Projekt dient der Automatisierung des Berichtshefts für Azubi.

## Aufgabenstellung

Entwicklung einer Anwendung, die folgende Aufgaben automatisiert:

Datenabfrage:
-Sichere Erfassung der Zugangsdaten (Webinterface/Console) und Abruf der WorkLog-Daten der letzten x Wochen über die 7pace Time Tracker API.

Datenverarbeitung:
-Sortierung der abgerufenen Daten nach Datum und Backlog Items. Anhand der WorkItemId erfolgt eine zusätzliche Abfrage, um den Namen des entsprechenden Backlog Items zu ermitteln.

Reporting:
-Aggregation der täglichen Backlog Items inklusive Tracking-Zeit und Erstellung eines übersichtlichen PDF-Berichts.

Datenschutz:
-Die Anwendung muss sämtliche Vorgaben des deutschen Datenschutzes (DSGVO) erfüllen, insbesondere hinsichtlich sicherer Datenübertragung, Speicherung und Zugriffsbeschränkungen.


## Qualitätsziele

| Qualitätsmerkmal    | Anforderung                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------|
| Benutzbarkeit       | Das System sollte selbstverständlich bedienbar sein.                                                                         |
| Sicherheit          | Das System sollte den Grundlegenden Sicherheitsanforderung gerecht werden                                                    |
| Wartbarkeit         | Die Dokumentation des Projekts soll dafür sorgen das andere Entwickler dieses Projekt weiter bearbeiten können ohne Probleme |
| Kompatibilität      | Das Projekt sollte auf allen bekannten Betriebssystem funktionieren, die einzige Voraussetzung ist dieNutzung der 7 Pace API |

## Stakeholder

| Stakeholder             | Beschreibung                                                                                           | Hinweise |
|-------------------------|--------------------------------------------------------------------------------------------------------|----------|
| Projektleitung          | Tom August                                                                                             |          |
| Umsetzung               | Tom August                                                                                             |          |
| Qualitätssicherung      | Tom August                                                                                             |          |
| Produktverantwortlicher | Tom August                                                                                             |          |
| Endanwender             | Azubis der Firma VIOSYS (oder andere die 7 Pace nutzen)                                                |          |

## Personas / Anwendungsbeschreibung


{type="narrow" sorted="desc"}
Beispiel #1 - Kevin Azubi 1. Lehrjahr
: Kevin ist Azubi bei der Firma XY und macht eine Ausbildung zum XY
: Zum erfassen der Arbeitszeiten nutzt seine Firma den 7 Pace Time Tracker
: Jede Woche muss er seinen Chef ein Berichtsheft geben in Form einer PDF
: Dafür nutzt unser Projekt um diese Arbeit zu vereinfachen

## Querverweise

tdoku.viosys.de/bruchprojekt)