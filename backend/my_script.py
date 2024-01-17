import fitz  # PyMuPDF
import Lenguaje
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_error_type(rule_id):
    if rule_id.startswith('MORFOLOGIK_RULE_ES'):
        return 'Ortografía'
    elif rule_id == 'AGREEMENT_DET_NOUN':
        return 'Error gramatical'
    elif rule_id == 'ES_SIMPLE_REPLACE_SIMPLE_TAMBIEN':
        return 'Error gramatical'
    else:
        return 'Desconocido'

def highlight_errors(text, matches):
    lines = text.split('\n')

    for i, line in enumerate(lines):
        error_info = []

        for match in matches:
            start, end = match.offset, match.offset + match.errorLength
            if start <= len(line) and end <= len(line):
                error_type = get_error_type(match.ruleId)
                error_info.append((start, end, error_type, match.message))

        error_info.sort()

        corrected_line = []
        last_end = 0

        for start, end, error_type, message in error_info:
            if error_type == 'Ortografía':
                corrected_line.extend(line[last_end:start])
                corrected_line.append(f"\033[94m{line[start:end]}\033[0m")  # Azul para errores ortográficos
                last_end = end
            elif error_type == 'Error gramatical':
                corrected_line.extend(line[last_end:start])
                corrected_line.append(f"\033[92m{line[start:end]}\033[0m")  # Verde para errores gramaticales
                last_end = end

            # Imprimir información adicional sobre el error
            print(f"{line[start:end]} - {error_type} ({message})")

        corrected_line.extend(line[last_end:])
        print(''.join(corrected_line))

def highlight_errors_pdf(text, matches, pdf_filename='output.pdf'):
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Ajustar el diseño para que quepa en tamaño A4
    page_width, page_height = letter
    margin = 50
    max_line_length = page_width - 2 * margin

    lines = text.split('\n')

    for i, line in enumerate(lines):
        error_indices = set()

        for match in matches:
            start, end = match.offset, match.offset + match.errorLength
            if start <= len(line) and end <= len(line):
                error_indices.update(range(start, end))

        x, y = margin, page_height - (i + 1) * 15
        for j, char in enumerate(line):
            if j in error_indices:
                pdf.setFillColorRGB(1, 0, 0)  # Rojo para errores
            else:
                pdf.setFillColorRGB(0, 0, 0)  # Negro para texto normal

            pdf.drawString(x, y, char)
            x += pdf.stringWidth(char, "Helvetica", 12)

            # Envolver texto a la siguiente línea si excede max_line_length
            if x > max_line_length:
                x = margin
                y -= 15

        pdf.drawString(margin, y - 15, '\n')  # Mover a la siguiente línea

    pdf.save()

# Tu código original
tool = Lenguaje.LanguageToolPublicAPI('es')

# Cambios para trabajar con archivos PDF
input_filename = 'texto.pdf'  # Reemplaza 'tu_archivo.pdf' con el nombre de tu archivo

try:
    pdf_document = fitz.open(input_filename)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    matches = tool.check(text)

    # Resaltar errores en el texto original y mostrar el texto corregido con colores diferentes
    highlight_errors(text, matches)

    # Guardar el texto con errores resaltados en un PDF
    output_pdf_filename = 'output.pdf'  # Puedes cambiar 'output.pdf' al nombre que desees para el PDF
    highlight_errors_pdf(text, matches, pdf_filename=output_pdf_filename)

finally:
    pdf_document.close()
