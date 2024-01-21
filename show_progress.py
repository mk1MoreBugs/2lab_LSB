def show_progress(count, total):
    progress = count / total * 100
    if progress % 10 == 0:
        print("Обработано пикселей:", int(progress), "%")
