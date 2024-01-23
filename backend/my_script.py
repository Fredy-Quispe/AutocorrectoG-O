import os
import fitz 
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

def analizar_documento_pdf(archivo, output_filename='output.pdf'):
    tool = Lenguaje.LanguageToolPublicAPI('es')

    try:
        archivo.save(os.path.join('uploads', archivo.filename))

        pdf_document = fitz.open(os.path.join('uploads', archivo.filename))
        text = ""

        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()

        matches = tool.check(text)

        output_pdf_filepath = highlight_errors_pdf(text, matches, pdf_filename=output_filename)

        pdf_document.close()

        return output_pdf_filepath

    except fitz.FileNotFoundError as e:
        print(f'Error en el servidor: Archivo no encontrado: {str(e)}')
        return {'error': f'Archivo no encontrado: {str(e)}'}, 404

    except Exception as e:
        print(f'Error interno del servidor: {str(e)}')
        return {'error': f'Error interno del servidor: {str(e)}'}, 500  
        

def highlight_errors_pdf(text, matches, pdf_filename='output.pdf'):

    pdf_filepath = os.path.join('resultados', pdf_filename.replace('\\', '/'))
    pdf = canvas.Canvas(pdf_filepath, pagesize=letter)
    pdf.setFont("Helvetica", 12)

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
                pdf.setFillColorRGB(1, 0, 0) 
            else:
                pdf.setFillColorRGB(0, 0, 0) 

            pdf.drawString(x, y, char)
            x += pdf.stringWidth(char, "Helvetica", 12)

            if x > max_line_length:
                x = margin
                y -= 15

        pdf.drawString(margin, y - 15, '\n') 

    pdf.save()
    print(f'Ruta del archivo resultante: {pdf_filepath}')
    return pdf_filepath