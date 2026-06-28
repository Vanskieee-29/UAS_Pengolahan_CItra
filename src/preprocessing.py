"""
=========================================================
PREPROCESSING MODULE
=========================================================
Berisi fungsi-fungsi preprocessing citra digital.

Author : Davan
Project : UAS Pengolahan Citra Digital
=========================================================
"""

import cv2
import numpy as np


def rgb_to_grayscale(image):
    """
    Mengubah citra RGB menjadi Grayscale.

    Parameter
    ---------
    image : numpy.ndarray

    Return
    ------
    grayscale image
    """

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    return gray


def rgb_to_binary(image, threshold=127):
    """
    Mengubah citra RGB menjadi Binary.

    Parameter
    ---------
    image : numpy.ndarray
    threshold : int

    Return
    ------
    binary image
    """

    gray = rgb_to_grayscale(image)

    _, binary = cv2.threshold(
        gray,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    return binary


def negative_image(image):
    """
    Membuat citra negatif.
    (Opsional untuk pengembangan)
    """

    return 255 - image


def resize_image(image, width=500):
    """
    Resize image dengan menjaga aspect ratio.
    """

    h, w = image.shape[:2]

    ratio = width / w

    new_height = int(h * ratio)

    resized = cv2.resize(
        image,
        (width, new_height),
        interpolation=cv2.INTER_AREA
    )

    return resized