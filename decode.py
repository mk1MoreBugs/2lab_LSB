from stegano import lsb


def decode(src):
    return lsb.reveal(src)
