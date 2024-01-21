from stegano import lsb


def encode(src, path_save, message):
    secret = lsb.hide(src, message)
    secret.save(path_save)
