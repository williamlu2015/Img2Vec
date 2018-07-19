from PIL import Image

from util.io import write_file


def image_to_racket(image_filename, racket_filename):
    with Image.open(image_filename) as image:
        image = image.convert("RGBA")
        racket_string = to_racket(image)

    write_file(racket_filename, racket_string)


def to_racket(image, cell_width=3, cell_height=3):
    result = "#lang htdp/bsl\n\n(require 2htdp/image)\n\n"

    width, height = image.size

    columns = []
    for x0 in range(0, width, cell_width):
        rectangles = []
        for y0 in range(0, height, cell_height):
            x1 = min(width, x0 + cell_width)
            y1 = min(height, y0 + cell_height)

            rectangle = to_rectangle(image, x0, y0, x1, y1)
            rectangles.append(rectangle)

        column = "(above\n  " + "\n  ".join(rectangles) + ")"
        columns.append(column)

    result += "(beside\n " + "\n ".join(columns) + ")"
    return result


def to_rectangle(image, x0, y0, x1, y1):
    rgba_sum = [0, 0, 0, 0]

    for x in range(x0, x1):
        for y in range(y0, y1):
            rgba_color = image.getpixel((x, y))
            for i, value in enumerate(rgba_color):
                rgba_sum[i] += value

    width = x1 - x0
    height = y1 - y0
    num_pixels = width * height
    rgba_average = [_sum // num_pixels for _sum in rgba_sum]

    return f"(rectangle {width} {height} \"solid\" {to_color(rgba_average)})"


def to_color(rgba):
    return f"(color {rgba[0]} {rgba[1]} {rgba[2]} {rgba[3]})"
