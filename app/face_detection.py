
import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def detect_faces(image_path: str):
    # Set up Azure Face API client
    face_client = FaceClient(
        endpoint=os.getenv("AZURE_FACE_API_ENDPOINT"),
        credentials=CognitiveServicesCredentials(os.getenv("AZURE_FACE_API_KEY"))
    )

    # Detect faces in the image
    with open(image_path, "rb") as image_file:
        detected_faces = face_client.face.detect_with_stream(
            image=image_file,
            return_face_attributes=["age", "gender", "emotion", "glasses", "hair", "smile"],
            detection_model="detection_03",
            recognition_model="recognition_04"
        )

    # Format the results
    results = []
    for face in detected_faces:
        results.append({
            "face_id": face.face_id,
            "age": face.face_attributes.age,
            "gender": face.face_attributes.gender,
            "emotion": face.face_attributes.emotion,
            "glasses": face.face_attributes.glasses,
            "hair": face.face_attributes.hair.__dict__,
            "smile": face.face_attributes.smile,
            "face_rectangle": {
                "top": face.face_rectangle.top,
                "left": face.face_rectangle.left,
                "width": face.face_rectangle.width,
                "height": face.face_rectangle.height
            }
        })

    return results
