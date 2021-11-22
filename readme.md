
# What is this?

This is a python3 tool that you can use to generate an Anki deck (an .apkg file, in other words) which maps Toaq vocabulary words to sets of images, with no English involved.

# Installation

    1. Clone this repository.
    2. Make sure you have genanki installed (`pip3 install genanki`).
    3. Run `make run` to make sure everything works. This should produce a file called "toaq.apkg" which can be directly imported into Anki.

# Adding more words

Here is the process for adding additional vocabulary words:

    1. Choose a word to add, for example "rua".
    2. Find images (for example, using Google) of things that are rua.
    3. Save those images to the media folder with the names "rua1.png", "rua2.jpg", etc (any reasonable image format should work).
    4. Repeate steps 1-3 as many times as desired.
    5. Type `make run` again to regenerate the APKG file.

