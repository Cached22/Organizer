from google.cloud import vision
import io

class ObjectRecognitionService:
    def __init__(self, google_credentials_path):
        self.client = vision.ImageAnnotatorClient.from_service_account_json(google_credentials_path)

    def recognize_objects(self, image_path):
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = self.client.object_localization(image=image)
        objects = response.localized_object_annotations

        recognized_objects = []
        for object_ in objects:
            recognized_objects.append({
                'name': object_.name,
                'score': object_.score,
                'bounding_poly': [(vertex.x, vertex.y) for vertex in object_.bounding_poly.normalized_vertices]
            })

        if response.error.message:
            raise Exception(f'Error recognizing objects: {response.error.message}')

        return recognized_objects

# Example usage:
# object_recognition_service = ObjectRecognitionService('path/to/google_credentials.json')
# recognized_objects = object_recognition_service.recognize_objects('path/to/image.jpg')
# print(recognized_objects)