from PIL import Image
import numpy as np

from open_img import open_img
from show_progress import show_progress


def decode(src, stop_world):
    message_found = False

    img = open_img(src)
    array = np.array(list(img.getdata()))

    n = 3
    if img.mode == 'RGBA':
        n = 4

    print("decode...")
    total_pixels = array.size
    hidden_bits = np.empty(total_pixels, dtype=np.byte)
    index = 0
    for p in range(total_pixels//n):
        for q in range(0, n):
            hidden_bits[index] = bin(array[p][q])[-1]
            index += 1

        show_progress(p, total_pixels/n)

    message = ""
    for i in range(0, hidden_bits.size, 8):

        arr = hidden_bits[i:i+8].astype(str)
        i_char = chr(int("".join(arr), 2))
        message += i_char
        if stop_world in message:
            message_found = True
            message = message[:-1 * len(stop_world)]
            break

    if message_found:
        print("Скрытое сообщение:", message)
    else:
        print("Скрытое сообщение не найдено")
