from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf(grouped_data, kw, name, filename="Ausbildungsnachweis.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Layout-Einstellungen
    margin = 50
    y_position = height - margin
    line_height = 15
    section_gap = 10

    # Überschrift NUR auf der ersten Seite
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - margin, f"Ausbildungsnachweis KW {kw} - {name}")
    y_position = height - margin - 30  # Abstand nach der Überschrift

    # Wochentage in Reihenfolge
    tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

    for tag in tage:
        # Überspringe leere Tage
        if tag not in grouped_data or not grouped_data[tag]:
            continue

        # Prüfe, ob genug Platz für den nächsten Tag ist (mind. 2 Einträge + Abstände)
        if y_position < margin + (3 * line_height + 2 * section_gap):
            c.showPage()
            y_position = height - margin  # Neue Seite, ohne Headline

        # Wochentag als Überschrift
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y_position, tag)
        y_position -= line_height

        # Einträge gruppieren nach Aufgabe
        aufgaben = {}
        for e in grouped_data[tag]:
            if e['title'] not in aufgaben:
                aufgaben[e['title']] = []
            aufgaben[e['title']].append(e)

        # Einträge schreiben
        for aufgabe, eintraege in aufgaben.items():
            # Prüfe, ob genug Platz für die nächste Aufgabe + Einträge
            needed_space = (len(eintraege) + 1) * line_height + section_gap
            if y_position - needed_space < margin:
                c.showPage()
                y_position = height - margin  # Neue Seite, ohne Wochentag zu wiederholen

            # Aufgabenname
            c.setFont("Helvetica", 11)
            c.drawString(margin, y_position, aufgabe)
            y_position -= line_height

            # Zeitangaben
            c.setFont("Helvetica", 10)
            for e in eintraege:
                # Falls kein Platz mehr, neue Seite
                if y_position < margin + line_height:
                    c.showPage()
                    y_position = height - margin

                start = e['startTime'].strftime("%H:%M")
                ende = e['endTime'].strftime("%H:%M")
                dauer = str(e['time'])[-8:-3]  # HH:MM Format

                text = f"{start} - {ende} ({dauer})"
                if e['Comment']:
                    text += f" - {e['Comment']}"

                c.drawString(margin + 20, y_position, text)
                y_position -= line_height

            y_position -= section_gap  # Abstand nach einer Aufgabe

        y_position -= section_gap  # Abstand nach einem Tag

    c.save()