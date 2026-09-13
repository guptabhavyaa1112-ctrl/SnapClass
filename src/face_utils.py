import face_recognition
import numpy as np
import io


def get_face_encoding(image_bytes):
    """
    Takes raw image bytes (from st.camera_input), returns a 128-number
    face encoding as a plain Python list, or None if no face was found.
    """
    image = face_recognition.load_image_file(io.BytesIO(image_bytes))
    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
        return None
    return encodings[0].tolist()


def compare_encoding(known_encoding, unknown_encoding, tolerance=0.5):
    """Returns True if the two encodings likely belong to the same person."""
    known = np.array(known_encoding)
    unknown = np.array(unknown_encoding)
    distance = np.linalg.norm(known - unknown)
    return distance <= tolerance

def get_all_face_encodings(image_bytes):
    """
    Takes raw image bytes, returns a list of face encodings (one per person)
    found in the photo. Used for group/classroom photos with multiple people.
    """
    image = face_recognition.load_image_file(io.BytesIO(image_bytes))
    encodings = face_recognition.face_encodings(image)
    return [e.tolist() for e in encodings]

