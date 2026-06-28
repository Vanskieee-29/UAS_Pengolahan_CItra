"""
=========================================================
FILTERING MODULE
=========================================================
Berisi fungsi-fungsi filtering citra digital.

Author  : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2
import numpy as np


# =========================================================
# Mean Filter
# =========================================================

def mean_filter(image, kernel_size=5):
    """
    Menghaluskan citra menggunakan Mean Filter.

    Parameters
    ----------
    image : ndarray
    kernel_size : int

    Returns
    -------
    ndarray
    """

    return cv2.blur(image, (kernel_size, kernel_size))


# =========================================================
# Median Filter
# =========================================================

def median_filter(image, kernel_size=5):
    """
    Mengurangi noise Salt & Pepper menggunakan
    Median Filter.
    """

    return cv2.medianBlur(image, kernel_size)


# =========================================================
# Gaussian Filter
# =========================================================

def gaussian_filter(image, kernel_size=5):
    """
    Menghaluskan citra menggunakan Gaussian Filter.
    """

    return cv2.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        0
    )