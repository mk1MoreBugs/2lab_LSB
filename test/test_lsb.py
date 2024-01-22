import os

from encode import encode
from decode import decode


SRC = "./test_image.jpg"
PATH_RESULT = "./result.png"
MESSAGE = "Hello world!"


def test_encode_file_is_exist():

    if os.path.exists(PATH_RESULT) is True:
        os.remove(PATH_RESULT)
    encode(SRC, PATH_RESULT, MESSAGE)
    assert os.path.exists(PATH_RESULT) is True


def test_decode_give_hide_text():
    encode(SRC, PATH_RESULT, MESSAGE)
    assert decode(PATH_RESULT) == MESSAGE
