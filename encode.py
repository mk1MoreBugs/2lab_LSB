import numpy as np

from open_img import open_img
from save_img import save_img
from show_progress import show_progress


def encode(src, message, dest, stop_world):
    print("Открываем изображение...")
    img = open_img(src)
    width, height = img.size
    array = np.array(list(img.getdata()))

    n = 3
    if img.mode == 'RGBA':
        n = 4

    total_pixels = array.size

    message += stop_world
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("Ошибка: необходим файл большего объёма")

    else:
        index = 0
        for p in range(total_pixels//n):
            for q in range(0, n):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[:-1] + b_message[index], 2)
                    index += 1

            show_progress(p, total_pixels/n)

        array = array.reshape(height, width, array.shape[1])
        save_img(array, dest, img.mode)
        img.close()
        print("Изображение успешно зашифровано")
