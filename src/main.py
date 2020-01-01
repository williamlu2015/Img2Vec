from root import from_root
from src.img2fn import image_to_function
from src.img2rkt import image_to_racket
from src.img2svd import image_to_svd


def main():
    image_to_racket(from_root("input/ttnr.png"), from_root("output/ttnr.rkt"))
    image_to_svd(from_root("input/ttnr.png"), from_root("output/ttnr_svd.png"))
    image_to_svd(from_root("input/anstee.gif"), from_root("output/anstee_svd.gif"))
    image_to_function(from_root("input/cropped-eugenia.jpg"), from_root("output/cropped-eugenia_fn.jpg"))


if __name__ == "__main__":
    main()
