"""
=========================================================
FACE DETECTION MODULE
=========================================================
Berisi fungsi deteksi wajah menggunakan Haar Cascade.

Author  : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2

CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

def detect_face(image):
    """
    Deteksi wajah menggunakan Haar Cascade.

    Parameters
    ----------
    image : ndarray (RGB)

    Returns
    -------
    result : ndarray
    face_count : int
    """

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    face_cascade = cv2.CascadeClassifier(
        CASCADE_PATH
    )

    print(CASCADE_PATH)
    print(face_cascade.empty())

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(80, 80)
    )

    print("Jumlah wajah:", len(faces))

    result = image.copy()

    for (x, y, w, h) in faces:

        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    return result, len(faces)