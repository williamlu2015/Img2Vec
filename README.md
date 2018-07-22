# Img2Vec
A collection of three Python scripts that convert image files to various vector graphics formats.
* image_to_racket() converts the input image to Racket code that uses Beginning Student Language's 2htdp/image API to draw the input image
    * Before running the generated Racket code, in DrRacket, go to Racket -> Limit Memory and select Unlimited to prevent "Out of Memory" errors in DrRacket.
* image_to_svd() converts the input image into a lower-rank approximation using Singular Value Decomposition
* image_to_function() converts the input image into a matplotlib plot that uses only piecewise sine functions of varying frequencies to represent lighter and darker pixels
    * Limit the dimensions of the input image to 150x150 to ensure that image_to_function() runs in a reasonable time.
