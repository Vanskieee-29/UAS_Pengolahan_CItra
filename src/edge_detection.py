"""
=========================================================
EDGE DETECTION MODULE
=========================================================
Berisi fungsi-fungsi deteksi tepi citra.

Author  : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2
import numpy as np


# =========================================================
# Sobel Edge Detection
# =========================================================

def sobel_edge(image):
    """
    Mendeteksi tepi citra menggunakan operator Sobel.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()

    sobel_x = cv2.Sobel(
        gray,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    sobel_y = cv2.Sobel(
        gray,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    magnitude = cv2.magnitude(sobel_x, sobel_y)

    magnitude = np.uint8(
        np.clip(magnitude, 0, 255)
    )

    return magnitude


# =========================================================
# Canny Edge Detection
# =========================================================

def canny_edge(
        image,
        threshold1=100,
        threshold2=200):
    """
    Mendeteksi tepi citra menggunakan metode Canny.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()

    edge = cv2.Canny(
        gray,
        threshold1,
        threshold2
    )

    return edge