from flask import Blueprint, request, jsonify
from .views import upload_image, recognize_objects, generate_optimal_layout
from .schemas import LayoutSchema
from .utils.error_handling import handle_error

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400
        if file:
            response = upload_image(file)
            return jsonify(response), 200
    except Exception as e:
        return handle_error(e)

@api_blueprint.route('/recognize', methods=['POST'])
def recognize():
    try:
        image_data = request.get_json()
        if not image_data:
            return jsonify({'message': 'No image data provided'}), 400
        response = recognize_objects(image_data)
        return jsonify(response), 200
    except Exception as e:
        return handle_error(e)

@api_blueprint.route('/optimize', methods=['POST'])
def optimize():
    try:
        layout_data = request.get_json()
        if not layout_data:
            return jsonify({'message': 'No layout data provided'}), 400
        # Validate layout data against schema
        errors = LayoutSchema().validate(layout_data)
        if errors:
            return jsonify(errors), 400
        response = generate_optimal_layout(layout_data)
        return jsonify(response), 200
    except Exception as e:
        return handle_error(e)