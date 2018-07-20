import numpy as np
from PIL import Image
from numpy.linalg import svd

from util.io import write_image


def image_to_svd(input_filename, output_filename, rank=20):
    with Image.open(input_filename) as raw_input_image:
        input_image = raw_input_image.convert("RGB")   # technically not
        # necessary since raw_input_image.mode == "RGB" by default
        input_array = np.asarray(input_image)

    raw_output_array = _array_to_svd(input_array, rank)
    output_array = raw_output_array.astype("uint8")

    output_image = Image.fromarray(output_array, "RGB")   # technically "RGB" is
    # not necessary since mode can be automatically determined from input type
    write_image(output_filename, output_image)


def _array_to_svd(input_array, rank):
    input_layers = [
        layer_array[:, :, 0]
        for layer_array in np.split(input_array, 3, axis=2)
    ]

    output_layers = [
        _layer_to_svd(input_layer, rank)
        for input_layer in input_layers
    ]
    output_array = np.stack(output_layers, axis=2)
    return output_array


def _layer_to_svd(M, rank):
    U, S, VT = svd(M)

    U_trunc = U[:, :rank]
    S_trunc = S[:rank]
    VT_trunc = VT[:rank, :]

    TSVD = np.dot(U_trunc, np.dot(np.diag(S_trunc), VT_trunc))
    return TSVD
