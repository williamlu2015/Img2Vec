import numpy as np
from PIL import Image

from util.io import write_file


def image_to_racket(image_filename, racket_filename):
    """
    Produces Racket code that draws the image at image_filename. Saves the
    Racket code to the file at racket_filename.
    :param image_filename: the path to the image to produce Racket code for
    :param racket_filename: the file to save the Racket code at
    :return: None
    """
    with Image.open(image_filename) as image:
        image = image.convert("RGB")   # technically not necessary since
        # image.mode == "RGB" by default
        array = np.asarray(image)
        racket_string = _to_racket(array)

    write_file(racket_filename, racket_string)


def _to_racket(array, cell_width=3, cell_height=3):
    """
    Produces Racket code that approximates the given RGB array. Groups of
    adjacent pixels in the array are averaged in the Racket code.
    :param array: the RGB array to produce Racket code for
    :param cell_width: the number of horizontally adjacent pixels to average
    :param cell_height: the number of vertically adjacent pixels to average
    :return: the produced Racket code, as a string
    """
    result = "#lang htdp/bsl\n\n(require 2htdp/image)\n\n"

    height, width, _ = array.shape

    rows = []
    for y0 in range(0, height, cell_height):
        rectangles = []
        for x0 in range(0, width, cell_width):
            x1 = min(width, x0 + cell_width)
            y1 = min(height, y0 + cell_height)

            rectangle = _to_rectangle(array, x0, y0, x1, y1)
            rectangles.append(rectangle)

        row = "(beside\n  " + "\n  ".join(rectangles) + ")"
        rows.append(row)

    result += "(above\n " + "\n ".join(rows) + ")"
    return result


def _to_rectangle(array, x0, y0, x1, y1):
    """
    Averages the colors of the pixels of array that have x-value in [x0, x1) and
    y-value in [y0, y1). Returns Racket code that draws a rectangle of the
    average color and size (x1 - x0) by (y1 - y0).
    :param array: the 3D array to average the pixels of
    :param x0: the left-bound (inclusive) of the pixels to average
    :param y0: the upper-bound (inclusive) of the pixels to average
    :param x1: the right-bound (exclusive) of the pixels to average
    :param y1: the lower-bound (exclusive) of the pixels to average
    :return: the Racket code that draws the rectangle
    """
    rgb_average = [
        int(round(np.average(array[y0:y1, x0:x1, layer])))
        for layer in range(3)
    ]

    width = x1 - x0
    height = y1 - y0
    return f"(rectangle {width} {height} \"solid\" {_to_color(rgb_average)})"


def _to_color(rgb):
    """
    Returns Racket code that produces a Racket color object with the given RGB
    values.
    :param rgb: a list of length 3, with the red, green, and blue values, in
    that order
    :return: the Racket code that produces the Racket color object
    """
    return f"(color {rgb[0]} {rgb[1]} {rgb[2]})"
