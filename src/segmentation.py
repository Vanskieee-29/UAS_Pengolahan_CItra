"""
=========================================================
SEGMENTATION MODULE
=========================================================
Berisi fungsi-fungsi segmentasi citra digital.

Author  : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2
import numpy as np


# =========================================================
# Otsu Thresholding
# =========================================================

def threshold_segmentation(image):
    """
    Segmentasi citra menggunakan
    Otsu Thresholding.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image.copy()

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return threshold


# =========================================================
# K-Means Segmentation
# =========================================================

def kmeans_segmentation(image, k=3):
    """
    Segmentasi citra menggunakan
    K-Means Clustering.
    """

    data = image.reshape((-1, 3))

    data = np.float32(data)

    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    _, labels, centers = cv2.kmeans(
        data,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)

    segmented = centers[labels.flatten()]

    segmented = segmented.reshape(image.shape)

    return segmented