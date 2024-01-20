from flask import Blueprint, request, jsonify
from services.object_recognition import recognize_objects
from services.optimization import generate_optimal_layout
from utils.error_handling import handle_error
from database.models import User, Item
from database.db import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400
        if file:
            # Assuming a function save_image exists to save the image to the server
            image_path = save_image(file)
            return jsonify({'message': UPLOAD_SUCCESS, 'image_path': image_path}), 200
    except Exception as e:
        return handle_error(e)

@api_blueprint.route('/recognize', methods=['POST'])
def recognize():
    try:
        image_path = request.json.get('image_path', '')
        if not image_path:
            return jsonify({'message': 'Image path is required'}), 400
        items = recognize_objects(image_path)
        return jsonify({'message': RECOGNITION_SUCCESS, 'items': items}), 200
    except Exception as e:
        return handle_error(e)

@api_blueprint.route('/optimize', methods=['POST'])
def optimize():
    try:
        items = request.json.get('items', [])
        dimensions = request.json.get('dimensions', {})
        if not items or not dimensions:
            return jsonify({'message': 'Items and dimensions are required'}), 400
        layout = generate_optimal_layout(items, dimensions)
        return jsonify({'message': OPTIMIZATION_SUCCESS, 'layout': layout}), 200
    except Exception as e:
        return handle_error(e)

@api_blueprint.route('/save', methods=['POST'])
def save_user_data():
    try:
        user_data = request.json
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User data saved successfully'}), 200
    except Exception as e:
        return handle_error(e)

def save_image(file):
    # This function should save the file and return the path where it was saved
    # Placeholder for actual image saving logic
    filename = secure_filename(file.filename)
    filepath = os.path.join('path_to_save_images', filename)
    file.save(filepath)
    return filepath

# Import this at the end to avoid circular imports
from utils.logging import log_event

@api_blueprint.errorhandler(Exception)
def handle_exception(error):
    log_event(str(error))
    return jsonify({'message': ERROR_MESSAGE, 'error': str(error)}), 500
