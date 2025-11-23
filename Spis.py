while True:
    inp=input('Введи число')

    try:
        inp=int(inp)
        ret=inp **3
        print(f'3 раза умноженное число{ret}')
    except:
        print(f'Всё таки нужно ввести число, а вы вели"{inp}"')
    finally:
        print('Еще раз')

