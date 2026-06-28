"""
=========================================================
ENHANCEMENT MODULE
=========================================================
Berisi fungsi-fungsi peningkatan kualitas citra.

Author  : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2
import numpy as np


# =========================================================
# Histogram Equalization
# =========================================================

def histogram_equalization(image):
    """
    Meningkatkan kontras citra menggunakan
    Histogram Equalization.
    """

    if len(image.shape) == 2:

        return cv2.equalizeHist(image)

    ycrcb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)

    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

    result = cv2.cvtColor(
        ycrcb,
        cv2.COLOR_YCrCb2RGB
    )

    return result


# =========================================================
# Contrast Stretching
# =========================================================

def contrast_stretching(image):
    """
    Meningkatkan kontras menggunakan
    Min-Max Normalization.
    """

    img = image.astype(np.float32)

    min_val = np.min(img)
    max_val = np.max(img)

    stretched = (img - min_val) * 255 / (max_val - min_val)

    stretched = np.clip(stretched, 0, 255)

    return stretched.astype(np.uint8)


# =========================================================
# Brightness Adjustment
# =========================================================

def brightness_adjustment(image, value=40):
    """
    Menambah brightness citra.

    value > 0  = lebih terang

    value < 0  = lebih gelap
    """

    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2HSV
    )

    h, s, v = cv2.split(hsv)

    v = np.clip(v + value, 0, 255).astype(np.uint8)

    hsv = cv2.merge((h, s, v))

    result = cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2RGB
    )

    return result