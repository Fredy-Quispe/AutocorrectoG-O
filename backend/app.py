from flask import Flask, request, jsonify, send_from_directory
from pdf2image import convert_from_path
from flask_cors import CORS
from os.path import join

import os
from my_script import analizar_documento_pdf

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No se proporcionó un archivo'}), 400

    document = request.files['document']

    try:
        resultados = analizar_documento_pdf(document)
        print(f'Nombre del archivo resultante desde backend: {resultados}')
        return jsonify({'message': 'Análisis ortográfico completado', 'result_filename': resultados})

    except FileNotFoundError as e:
        print(f'Error en el servidor: Archivo no encontrado: {str(e)}')
        return jsonify({'error': f'Archivo no encontrado: {str(e)}'}), 404
    
    except Exception as e:
        print(f'Error interno del servidor: {str(e)}')
        return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500

@app.route('/api/download/<path:filename>', methods=['GET'])
def download_file(filename):

    filepath = join(filename.replace('/', os.sep))

    print(f"BACK Intentando descargar el archivo desde la ruta: {filepath}")
    print(f"BACK contenido de filename: {filename}")

    if os.path.exists(filepath):
        return send_from_directory('.', filename, as_attachment=True)
    else:
        return jsonify({'error': f'Archivo no encontrado: {filename}', 'ruta_completa': filepath}), 404

if __name__ == '__main__':
    app.run(debug=True)