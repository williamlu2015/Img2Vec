import os


def write_file(filename, data):
    """
    Writes the given data string to the file with the given name. If the file (or any of the folders along its path)
    does not exist, it is created. If the file already exists, it is overwritten.
    :param filename: the path to the output file
    :param data: the string to write to the file
    :return: None
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(data)


def write_image(filename, image):
    """
    Saves the given Pillow image to the file with the given name. If the file (or any of the folders along its path)
    does not exist, it is created. If the file already exists, it is overwritten.
    :param filename: the path to the output file
    :param image: the Pillow image to save to the file
    :return: None
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)


def write_plot(filename, plt):
    """
    Saves the given matplotlib plot to the file with the given name. If the file (or any of the folders along its path)
    does not exist, it is created. If the file already exists, it is overwritten.
    :param filename: the path to the output file
    :param plt: the matplotlib plot to save to the file
    :return: None
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
