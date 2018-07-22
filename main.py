from src.img2fn import image_to_function
from src.img2rkt import image_to_racket
from src.img2svd import image_to_svd


def main():
    image_to_racket(
        "input/ttnr.png",
        "output/ttnr.rkt"
    )
    image_to_svd(
        "input/ttnr.png",
        "output/ttnr_svd.png"
    )
    image_to_svd(
        "input/anstee.gif",
        "output/anstee_svd.gif"
    )
    image_to_function(
        "input/cropped-eugenia.jpg",
        "output/cropped-eugenia_fn.jpg"
    )


if __name__ == "__main__":
    main()
