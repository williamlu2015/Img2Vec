from PIL import Image


# def image_to_svd(image_filename, U_filename, S_filename, VT_filename):
#     with Image.open(image_filename) as image:
#         image = image.convert("RGBA")
#         U, S, VT = to_svd(image)
#
#     write_file(U, U_filename)
#     write_file(S, S_filename)
#     write_sparse(VT, VT_filename)
