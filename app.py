from doctest import debug

from flask import Flask, request, jsonify, send_from_directory
import logging
import os

app = Flask(__name__)

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/malicious')
def serve_malicious_page():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/log', methods=['POST'])
def log_message():
    data = request.get_json()
    message = data.get('message', 'No message provided')

    # Log del messaggio
    app.logger.info(message)

    return jsonify({"status": "success", "message": "Log received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
