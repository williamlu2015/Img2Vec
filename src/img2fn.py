from math import pi, sin, ceil

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def image_to_function(input_filename, output_filename):
    with Image.open(input_filename) as raw_image:
        image = raw_image.convert("L")
        array = np.asarray(image)

    _array_to_function(array, output_filename)


def _array_to_function(array, output_filename):
    m, n = array.shape
    for i in range(m):
        for j in range(n):
            print(i, j)
            luminance = array[i, j]
            b = ceil((1 - luminance / 255) * 8)
            f = _factory(1, b, i, j)

            x_vec = np.linspace(j, j + 1, 1000, endpoint=True)
            y_vec = f(x_vec)

            lines = plt.plot(x_vec, y_vec)
            plt.setp(lines, linewidth=0.1, color="k")

    plt.axis("equal")
    plt.savefig(output_filename)


def _factory(a, b, i, j):
    def f(x):
        return a * sin(2 * pi * b * (x - j)) + 0.5 - i

    f_vec = np.vectorize(f)
    return f_vec
