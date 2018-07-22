import numpy as np
from PIL import Image
from numpy.linalg import svd

from util.io import write_image


def image_to_svd(input_filename, output_filename, rank=20):
    """
    Computes a lower-rank approximation of the image at input_filename using
    Singular Value Decomposition. Saves the approximation at output_filename.
    :param input_filename: the path to the image to approximate
    :param output_filename: the file to save the approximation to
    :param rank: the rank of the approximation
    :return: None
    """
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
    """
    Computes a lower-rank approximation of each layer of the given 3D matrix
    using Singular Value Decomposition. The layers are obtained by splitting the
    given 3D matrix along axis 2.
    :param input_array: the 3D matrix to approximate
    :param rank: the rank of the approximation
    :return: the lower-rank approximation of input_array
    """
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
    """
    Computes a lower-rank approximation of the given 2D matrix using Singular
    Value Decomposition.
    :param M: the 2D matrix to approximate
    :param rank: the rank of the approximation
    :return: the lower-rank approximation of the given matrix
    """
    U, S, VT = svd(M)

    U_trunc = U[:, :rank]
    S_trunc = S[:rank]
    VT_trunc = VT[:rank, :]

    TSVD = np.dot(U_trunc, np.dot(np.diag(S_trunc), VT_trunc))
    return TSVD
