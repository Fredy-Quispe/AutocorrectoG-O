from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import os
from my_script import analizar_documento_pdf

app = Flask(__name__)
CORS(app)

RESULT_DIR = 'resultados'
if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)

@app.route('/api/analyze', methods=['POST'])
def analyze_document():
    # Verificar si hay un archivo en la solicitud
    if 'document' not in request.files:
        return jsonify({'error': 'No se proporcionó un archivo'}), 400

    document = request.files['document']

    try:
        # Llamar a la función de análisis del documento PDF
        resultados = analizar_documento_pdf(document)

        # Devolver los resultados al frontend
        return jsonify({'message': 'Análisis ortográfico completado', 'result_filename': resultados})

    except FileNotFoundError as e:
        return jsonify({'error': f'Error al abrir el archivo: {str(e)}'}), 500

    except Exception as e:
        print(f"Error interno del servidor: {str(e)}")
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(RESULT_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)