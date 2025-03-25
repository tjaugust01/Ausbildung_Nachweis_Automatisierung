from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_worklog_pdf(works, output_pdf="worklogs.pdf"):
    weekdays_order = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setTitle("Worklogs nach Wochentag")

    page_width, _ = A4
    c.setFont("Helvetica", 16)
    c.drawCentredString(page_width / 2, 800, "Ausbildungsnachweis")

    c.setFont("Helvetica", 12)
    x_margin, y_position = 50, 775

    for day in weekdays_order:
        c.drawString(x_margin, y_position, f"{day}:")
        y_position -= 20

        day_worklogs = [wl for wl in works if wl["weekday"] == day]
        if not day_worklogs:
            c.drawString(x_margin + 10, y_position, "Keine Einträge")
            y_position -= 40
        else:
            for wl in day_worklogs:
                c.drawString(x_margin + 10, y_position, f"{wl['startTime']} - {wl['endTime']} ({wl['time']})")
                y_position -= 20
                c.drawString(x_margin + 10, y_position, wl["title"])
                y_position -= 20
                if wl["Comment"]:
                    c.drawString(x_margin + 10, y_position, wl["Comment"])
                    y_position -= 20
                y_position -= 20

        if y_position < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = 800

    c.showPage()
    c.save()
    print(f"PDF wurde erstellt: {output_pdf}")
