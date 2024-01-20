from flask import jsonify

def handle_error(error, status_code):
    """
    Generic error handler that logs the error and returns a JSON response.
    """
    # Log the error for debugging purposes
    log_event(str(error))

    # Return a JSON response with a generic error message and the status code
    return jsonify({
        'success': False,
        'message': ERROR_MESSAGE.format(error=str(error))
    }), status_code

def log_event(message):
    """
    Logs an event or error message to the console or a file.
    """
    # This function should be expanded to include logging to a file or external service
    print(message)  # Placeholder for actual logging

# Example usage of error handling in an API endpoint
# from flask import Flask, request
# app = Flask(__name__)
#
# @app.route('/upload', methods=['POST'])
# def upload_image():
#     try:
#         # Code to handle image upload
#         pass
#     except Exception as e:
#         return handle_error(e, 500)

ERROR_MESSAGE = "An error occurred: {error}"  # Placeholder for actual error messages
# The ERROR_MESSAGE format should be defined according to the shared dependencies and used consistently across the application.