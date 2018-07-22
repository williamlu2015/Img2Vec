from math import pi, sin, ceil

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from util.io import write_plot


def image_to_function(input_filename, output_filename):
    """
    Approximates the image at input_filename by plotting piecewise sine waves
    using matplotlib. Saves the approximation at output_filename.
    :param input_filename: the path to the image to approximate
    :param output_filename: the file to save the approximation to
    :return: None
    """
    with Image.open(input_filename) as raw_image:
        image = raw_image.convert("L")
        array = np.asarray(image)

    _array_to_function(array, output_filename)


def _array_to_function(array, output_filename):
    """
    Approximates the given 2D array of luminance values by plotting piecewise
    sine waves using matplotlib. Saves the approximation at output_filename.
    :param array: the 2D array of luminance values to approximate
    :param output_filename: the file to save the approximation to
    :return: None
    """
    m, n = array.shape
    for i in range(m):
        for j in range(n):
            luminance = array[i, j]
            b = ceil((1 - luminance / 255) * 50)
            f = _factory(1, b, i, j)

            x_vec = np.linspace(j, j + 1, 1000, endpoint=True)
            y_vec = f(x_vec)

            lines = plt.plot(x_vec, y_vec)
            plt.setp(lines, linewidth=0.1, color="k")

        print(f"Finished processing row {i}")

    ppi = 218
    fig = plt.gcf()
    fig.set_size_inches(n * 100 / ppi, m * 100 / ppi)

    plt.axis("equal")
    write_plot(output_filename, plt)


def _factory(a, b, i, j):
    """
    Returns the function f(x) = a * sin((2pi * b)(x - j)) + 0.5 - i.
    :param a: the amplitude of the sine wave
    :param b: the frequency of the sine wave
    :param i: the negative of the vertical shift of the sine wave, minus 0.5
    :param j: the phase shift of the sine wave
    :return: the sine wave
    """
    def f(x):
        return a * sin(2 * pi * b * (x - j)) + 0.5 - i

    f_vec = np.vectorize(f)
    return f_vec
