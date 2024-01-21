import PIL
from PIL import Image


def open_img(src):
    try:
        return Image.open(src)
    except FileNotFoundError:
        print("Файл не найден!")
    except PIL.UnidentifiedImageError:
        print("Изображение невозможно открыть и идентифицировать!")
