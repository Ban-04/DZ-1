import random

class Human:
    def __init__(self, healf, strange ):
        self.healf = healf
        self.stange = strange

class Moral:
    def __init__(self, morality=50):
        self.value = morality
        print(f"Нравственность: {self.value}")

    def change_morality(self, amount):
        self.value += amount
        self.value = max(0, min(100, self.value))
        print(f"Нравственность {amount} стало {self.value}")
        return True


class Gregari (Human):
    def __init__(self, health, strange, morality=50):
        super().__init__(health,strange )
        self.moral = Moral(morality)

class NotImplementedException(Exception):
    ...
def registratura(gregari):
    print(
        "Мед.сестра говорит:Здравствуйте, подготовьте документы и ваш талон.У вас нет талона, становитесь в очередь!!")
    gregari.moral.change_morality(-50)

    x = input("Продолжить стоять в очереди (1) или пойти за талоном (2), Пойти в кабинет врача (3) ")
    if x == '1':
        print("Ты решился постоять в очереди")
        gregari.moral.change_morality(25)
        print("Через час вы наконец попадаете к окну.")
    elif x == '2':
        print("Ты решился взять талон.")
        gregari.moral.change_morality(25)
        Talon(gregari)
    elif x == '3':
        print("Ты подумал, а что мне стоять и ждать в очереди")
        gregari.moral.change_morality(-75)
        Doctor(gregari)
    else:
        print("Вы не смогли выбрать число")
        gregari.moral.change_morality(0)

def Talon(gregari):
    print("Вы берёте талон после 1 человека, подходите к столу")
    gregari.moral.change_morality(100)

def Doctor(gregari):
    while True:

        print("Вы подошли к кабинету врача")
        s = input("Зайти в кабинет без очереди сказав: Я быстро и получить направление (1-2)?")
        s = int(s)
        win = random.randint(1, 2)
        if s == win:
            print("Поздравляем, удача на вашей стороне и врач выписал вам направление")
            gregari.moral.change_morality(-100)
            break

        else:
            print("Вам не повезло, врач понял ваши действия и выгнал вас из кабинета отправив вас в регистратуру.")

        repeat = input("Подождём минуту и попытаемся снова?")
        if repeat.strip().lower() == 'нет':
            break



print("Здравствуйте , не могли бы вы надеть бахилы?")

enter = input("Здравствуйте (Да/Нет)")

gregari = Gregari(100, 50, morality=50)

print ('Да' == enter)

if 'Да'== enter:
    print("Санитарка говорит:Спасибо вам за понимание.")

    choose = input("Куда вы направитесь?:регистратура (1), талон (2), врач (3)")

    try:
        if '1' == choose:
            registratura(gregari)


        elif '2' == choose:
            Talon(gregari)


        elif '3' == choose:
            Doctor(gregari)

    except NotImplementedException as err:
        print(f'Попробуйте позже: {err}')


elif 'Нет' == enter:
    print("Санитарка говорит:Без бахила не пройдёте.")
print("Ваши результаты:")
print(f"Нравственность {gregari.moral.value}")