# 1. Einführung und Ziele

## Was ist das Projekt

Beschreiben Sie das Projekt mit zwei bis drei Sätzen. Diese werden von allen Projektbeteiligten und Dritten Außenstehenden verstanden. 

> Die Projektbeschreibung ist eine Art Steckbrief und beschreibt Existenzgrund und -ziel des Projektes.
> {style="note"}

> Beispiel: Schüler der 7. Klasse müssen immer wieder gemeine Brüche kürzen. Dieses Webprojekt soll ihnen helfen, indem Brüche nachvollziehbar online gekürzt werden können.

Die folgenden Unterpunkte können auf extra Seiten ausgelagert werden, wenn deren Beschreibung dies erfordert (bspw. wenn die Auftragsbestätigung mehr als eine Position umfasst)! In diesem Fall ggf. auf der Einleitung heraus direkt darauf verlinken!

## Aufgabenstellung

Beschreibung der (vom Kunden) gestellten Aufgabe und wesentlicher Features. Hier können die Positionen der Auftragsbestätigung als Grundlage genutzt werden. Aus diesen sind mögliche [Randbedingungen](2-Randbedingungen.md), [Kontextabgrenzung](3-Kontextabgrenzung.md) und [Qualitätsanforderungen](10-Qualitätsanforderungen.md) auszuklammern.

> Beispiel: Erstellung einer Website mit einer Anwendung, welche die Eingabe des Zählers und Nenners eines gemeinen Bruches zulässt. Mit Klick auf den Button "Kürzen" soll der so spezifizierte gemeine Bruch gekürzt werden und der gekürzte Bruch als Ergebnis erscheinen.
> Features:
> - von jedem Nutzer online übers Web nutzbar
> - einfache Eingabe von Zähler und Nenner
> - berechnet auf Klick den größten gemeinsamen Teiler und gibt den gekürzten Bruch aus
> - behandelt Fehler wie bspw. "Teilung durch Null" und verhindert Falscheingaben bspw. Text statt Zahlen
> - unterstützt auch negative Brüche

## Qualitätsziele

> Passen Sie die folgende Tabelle auf die wirklich (mit dem Kunden) definierten Qualitätsmerkmale an und beschreiben Sie diese. Nennen Sie keine Qualitätsziele, die nicht mit dem Auftraggeber vereinbart sind!
> {style="warning"}

| Qualitätsmerkmal    | Anforderung                                                                                                                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Benutzbarkeit       | Ist die Software intuitiv zu bedienen, leicht zu erlernen, attraktiv? Verständlichkeit, Wiedererkennbarkeit, Erlernbarkeit, Bedienbarkeit, Fehlervermeidung, Ästhetik, Barrierefreiheit, Attraktivität       |
| Effizienz           | Antwortet die Software schnell hat sie einen hohen Durchsatz einen geringen Ressourcenverbrauch? Zeitverhalten, Verbrauchsverhalten, Kapazität                                                               |
| Funktionale Eignung | Sind die berechneten Ergebnisse genau genug Exakt ist die Funktionalität angemessen? Angemessenheit, Korrektheit, Vollständigkeit                                                                            |
| Sicherheit          | Ist das System sicher vor Angriffen? Sind Daten und Funktionen vor unberechtigten Zugriff geschützt? Vertraulichkeit, Nachweisbarkeit, Datenintegrität, Authentizität, Zurechenbarkeit                       |
| Wartbarkeit         | Ist die Software leicht zu ändern, erweitern, testen, verstehen? Lassen sich Teile wiederverwenden? Änderbarkeit , Erweiterbarkeit , Stabilität , WiedDie erverwendbarkeit , Analysierbarkeit , Testbarkeit. |
| Zuverlässigkeit     | Ist das System verfügbar, tolerant gegenüber Fehlern Komma nach Abstürzen schnell wieder hergestellt? Verfügbarkeit , Wiederherstellbarkeit , Fehlertoleranz , Reife7 6                                      |
| Übertragbarkeit     | Ist die Software leicht auf andere Systemumgebungen (zum Beispiel anderes OS) Übertragbar? Anpassbarkeit, Austauschbarkeit, Installierbarkeit, Koexistenz                                                    |
| Kompatibilität      | Ist die Software konform zu Standards, arbeitet sie gut mit anderen Softwareprodukten zusammen? Koexistenz, Interoperabilität                                                                                |

> Füllen Sie die folgende Tabelle mit Qualitätszielen und ordnen Sie jedem Ziel mind. ein Qualitätsmerkmal zu.
> 
> Checkliste für den Inhalt
> 1. Sind die Ziele konsistent zur Aufgabenstellung?
> 2. Sind die Ziele nach Wichtigkeit sortiert (das Wichtigste zuerst!)
> 3. Sind alle Qualitätsziele von den Stakeholdern akzeptiert?
>
> Die Qualitätsziele sind wichtig und werden in der Beschreibung der Lösungsstrategie wieder aufgegriffen!
> {style="warning"}

| Qualitätsziel             | Qualitätsmerkmal              | Motivation und Erläuterung                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nutzbarkeit für Jedermann | Benutzbarkeit, Kompatibilität | "Bruch kürzen" ist für jedermann im Browser nutzbar und intuitiv zu begreifen                                                                                                                                                                                                            |
| Unterstützung des Lernens | Funktionale Eignung           | Das Projekt soll Schülern helfen, zu verstehen wie "Brüche kürzen" funktioniert und sie bei der Kontrolle von Hausaufgaben unterstützen. redaktionell pflegbare Hilfen/Links zur Erklärung des Themas, Übungsaufgaben mit Kontroll-/Erfolgskontrolle. Eigene Hausaufgaben kontrollieren. |
| (Beschreibung des Ziels)  | (mind. ein Qualitätsmerkmal)| (Beschreibung des Ziels                                                                                                                                                                                                                                                                  |

## Stakeholder

| Stakeholder             | Beschreibung                       | Hinweise                                                  |
|-------------------------|------------------------------------|-----------------------------------------------------------|
| Projektleitung          | Name des Projektleiters bei VIOSYS |                                                           |
| Umsetzung               | Namen der beteiligten Softwareentwicker | hier jeweilige Verantwortlichkeiten/Schwerpunkte benennen |
| Qualitätssicherung      | Wer ist bei VIOSYS und beim Kunden dafür verantwortlich|                                                           |
| Produktverantwortlicher | Wer ist beim Kunden für das Projekt verantwortlich| i.d.R. Projektleiter beim Kunden                          |
| Endanwender             | Wer nutzt das System am Ende| hier auch ggf. verschiedene Rollen anschneiden            |
| Anwender beim Kunden    | Wer nutzt das Systen beim Kunden| hier auch ggf. verschiedene Rollen anschneiden            |
| Vertrieb                | Wer vertreibt das System später | i.d.R. nur für VIOSYS-PlugIns nötig                       |
| Marketing               | Wer erstellt Vertriebsmaterial bei VIOSYS oder beim Kunden | i.d.R. nur für VIOSYS-PlugIns nötig                       |
| Betrieb                 | Wer betreibt und supportet das System am Ende | |
| Nachbarprojekte         | Gibt es andere, in diesem Kontext relevante Softwareprojekte, die in eienr Beziehung zum System stehen| bspw. aufeinander aufbauende PlugIns |
| angebundene Systeme     | An welche Systeme ist das Softwareprojekt angebunden | |
| Wettbewerber            | Gibt es Wettbewerber(-produkte) | bspw. bei Shopware PlugIns |

## Personas / Anwendungsbeschreibung

> Die hier aufgeführten Anwendungsbeschreibungen bilden nicht den kompletten Funktionsumfang ab und dienen der grundsätzlichen Beschreibung der Projektfunktionalität bzw. des Projektziels
> {sytle="warning"}

Beschreiben Sie zwei bis drei Anwendungsszenarien an einer konkreten Person!

{type="narrow" sorted="desc"}
Beispiel #1 - Schüler 7. Klasse
: Max Meier ist Schüler an einer Leipziger Oberschule in der 7. Klasse.
: Er lernt gerade das Kürzen von Brüchen und möchte seine Hausaufgaben auf Korrektheit prüfen.
: Dazu geht er auf www.bruchkuerzen.de (unser Projekt) und kann dort Zähler und Nenner eines Bruches eingeben.
: Mit Klick auf "Kürzen" sieht er das Ergebnis, welches der mit seinem schriftlichen Ergebnis abgleichen kann.

## Querverweise

Das Softwareprojekt beruht auf folgenden Aufträgen/Tickets
- AB2023-40045: bruchkuerzen.de Onlineanwendung
- [T-2023123410238900025123](https://viosys.managed-otrs.com/agent/ticket/1467578): Division durch Null verhindern

VIOSYS Projektwiki
- [Projekt Bruch kürzen](https://www.projektdoku.viosys.de/bruchprojekt)