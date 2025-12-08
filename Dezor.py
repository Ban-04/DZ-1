from PIL import Image
while True:
    try:
        x=input("Название фотографии")
        im=Image.open("Images/"+x+".jpg")
        im.show()
        print(im.format, im.size, im.mode)
        break
    except Exception as e:
        print("Пропишите именно название", e)
while True:
    print("\nЧто сделать с картинкой? Применить эффект(1), Сохранить(2)")
    enter = input('Выберите числом 1, 2: ')
    if enter == '1':
        while True:
            try:
                a = input("Какой эффект используем? Черно-белое(1) , Отразить по горизонтали(2): ")
                if a == "1":
                    im = im.convert("L")
                    im.show()
                    break
                elif a == "2":
                    im = im.transpose(Image.FLIP_LEFT_RIGHT)
                    im.show()
                    break
                else:
                    print("'1' или '2'.")
            except Exception as e:
                print(f"Попробуйте снова: {e}")
        print("Как назовете изображение")
        y = input('введи новое имя файла ')
        try:
            im.save("Images/" + y + ".jpg")
            im.save("Images/" + y + ".jpg")
            break
        except Exception as d:
            print("Попробуй снова ошибка ", d)

    elif enter == '2':
         y = input('Новое имя файла :')
         im.save("Images/" + y + ".jpg")
         break
    else:
        print("Именно числом 1, 2")




