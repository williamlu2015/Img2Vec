import os


def write_file(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(data)


def write_image(filename, image):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)
