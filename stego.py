from decode import decode
from encode import encode

STOP_WORLD = "S.T.A.Y"


def stego():
    print("Выберите что хотите сделать")
    print("1: Зашифровать")
    print("2: Расшифровать")

    func = input()

    if func == '1':
        print("Введите путь исходного изображения")
        src = input()
        print("Введите сообщение, которое необходимо скрыть")
        message = input()
        dest = "./result.png"
        encode(src, message, dest, STOP_WORLD)

    elif func == '2':
        print("Введите путь к изображению с зашифрованным текстом")
        src = input()
        decode(src, STOP_WORLD)

    else:
        print("Ошибка: Вы ввели несуществующий вариант")
