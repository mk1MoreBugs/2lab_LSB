from PIL import Image


def save_img(array, dest, img_mode):
    enc_img = Image.fromarray(array.astype('uint8'), img_mode)
    enc_img.save(dest, quality=100)
    print("Путь сохраненного изображения: ./result.png")
