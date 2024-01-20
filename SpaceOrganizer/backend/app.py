from flask import Flask, request, jsonify
from services.object_recognition import recognizeObjects
from services.optimization import generateLayout
from database.db import initialize_db
from utils.error_handling import handle_error
from utils.logging import log_event

app = Flask(__name__)

# Load environment variables
app.config.from_envvar('APP_SETTINGS', silent=True)

# Initialize the database
initialize_db(app)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400
        if file:
            # Object recognition service
            items = recognizeObjects(file)
            return jsonify({'message': UPLOAD_SUCCESS, 'items': items}), 200
    except Exception as e:
        log_event(str(e))
        return handle_error(e)

@app.route('/optimize', methods=['POST'])
def optimize_layout():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        # Optimization service
        layout = generateLayout(data)
        return jsonify({'message': OPTIMIZATION_SUCCESS, 'layout': layout}), 200
    except Exception as e:
        log_event(str(e))
        return handle_error(e)

@app.route('/save', methods=['POST'])
def save_user_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        # Save user data to the database
        saveUserData(data)
        return jsonify({'message': 'User data saved successfully'}), 200
    except Exception as e:
        log_event(str(e))
        return handle_error(e)

if __name__ == '__main__':
    app.run(debug=True)