import fitz #PyMuPDF
import Lenguaje
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import jsonify


def get_error_type(rule_id):
    if rule_id.startswith('MORFOLOGIK_RULE_ES'):
        return 'Ortografía'
    elif rule_id == 'AGREEMENT_DET_NOUN':
        return 'Error gramatical'
    elif rule_id == 'ES_SIMPLE_REPLACE_SIMPLE_TAMBIEN':
        return 'Error gramatical'
    else:
        return 'Desconocido'

def analizar_documento_pdf(archivo, output_filename='output.pdf'):
    tool = Lenguaje.LanguageToolPublicAPI('es')

    try:
        pdf_document = fitz.open(archivo)
        text = ""

        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()

        matches = tool.check(text)

        # Guardar el texto con errores resaltados en un PDF
        output_pdf_filename = output_filename
        highlight_errors_pdf(text, matches, pdf_filename=output_pdf_filename)

        pdf_document.close()

        return jsonify({'message': 'Análisis ortográfico completado', 'result_filename': output_pdf_filename})

    except fitz.FileNotFoundError as e:
        # Manejar la excepción si el archivo no se encuentra
        return jsonify({'error': f'Archivo no encontrado: {str(e)}'}), 404

    except Exception as e:
        # Manejar otras excepciones
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500
        

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
