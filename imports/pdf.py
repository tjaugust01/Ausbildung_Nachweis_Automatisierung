from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

from datetime import datetime

pdfmetrics.registerFont(TTFont("DejaVuSans", "../fonts/DejaVuSans.ttf"))
registerFontFamily("DejaVuSans", normal="DejaVuSans")

WEEKDAY_ORDER = [
    "Montag", "Dienstag", "Mittwoch",
    "Donnerstag", "Freitag", "Samstag", "Sonntag",
]
def _seconds_to_hh_mm(seconds: int) -> str:
    minutes_total = round(seconds / 60)
    hours, minutes = divmod(minutes_total, 60)
    return f"{hours:02d}:{minutes:02d}"

def create_pdf(grouped_data, kw: int, name: str, filename: str = "./output/Ausbildungsnachweis.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    title_text = f"Ausbildungsnachweis – KW {kw} – {name}"
    c.setFont("DejaVuSans", 16)
    title_width = c.stringWidth(title_text, "DejaVuSans", 16)
    c.drawString((width - title_width) / 2, height - 25 * mm, title_text)

    y = height - 35 * mm
    line_height = 6 * mm
    indent = 10 * mm
    bullet_indent = 15 * mm

    c.setFont("DejaVuSans", 10)

    for weekday_key in WEEKDAY_ORDER:
        if weekday_key not in grouped_data:
            continue
        day_data = grouped_data[weekday_key]
        start_dt: datetime = day_data["start"]
        end_dt: datetime = day_data["end"]
        elemente = day_data.get("elemente", [])

        if y < 30 * mm:
            c.showPage()
            c.setFont("DejaVuSans", 10)
            y = height - 20 * mm

        day_name = weekday_key.capitalize()
        header = f"{day_name}: {start_dt.strftime('%H:%M')} – {end_dt.strftime('%H:%M')}"
        c.drawString(indent, y, header)
        y -= line_height

        for element in elemente:
            title = element["title"]
            duration_str = _seconds_to_hh_mm(int(element["duration"]))

            wrapped_lines = []
            max_line_width = width - (bullet_indent + 15 * mm)
            current_line = ""
            for word in title.split():
                test_line = (current_line + " " + word).strip()
                if c.stringWidth(test_line, "DejaVuSans", 10) < max_line_width:
                    current_line = test_line
                else:
                    wrapped_lines.append(current_line)
                    current_line = word
            if current_line:
                wrapped_lines.append(current_line)

            # erste Zeile mit Bullet & Dauer
            bullet_text = f"• {wrapped_lines[0]} ({duration_str})"
            c.drawString(bullet_indent, y, bullet_text)
            y -= line_height

            # Folgezeilen
            for cont_line in wrapped_lines[1:]:
                c.drawString(bullet_indent + 5 * mm, y, cont_line)
                y -= line_height

            if y < 20 * mm:
                c.showPage()
                c.setFont("DejaVuSans", 10)
                y = height - 20 * mm

        y -= line_height / 2

    c.save()
    return filename