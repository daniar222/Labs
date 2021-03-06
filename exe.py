'''
Вы попали к боту, который работает, как турагенство. Тут вы можете выбрать город, в который поедете.
Транспорт на котором доберётесь до цели, также выбрать билеты в транспорте.
Ну или получить ссылки на то, чтобы справиться самому.
'''




'''Функции def, принимают на вход номер
  выбранной позиции и возвращают ее название'''
def city(n):
    if n == '1':
        return 'Москва'
    elif n == '2':
        return 'Санкт-Петербург'
    elif n == '3':
        return 'Екатеринбург'
    elif n == '4':
        return 'Сочи'
    elif n == '5':
        return 'Краснодар'
    elif n == '6':
        return 'Новосибирск'
    elif n == '7':
        return 'Укажите город, в который вы хотите поехать'

def type_of_transport(n):
    if n == '1':
        return 'Самолёт'
    elif n == '2':
        return 'Поезд'
    elif n == '3':
        return 'Машина'
    elif n == '4':
        return 'Пешком'

def air_company(n):
    if n == '1':
        return 'Аэрофлот'
    elif n == '2':
        return 'S7'
    elif n == '3':
        return 'Red Wings'
    elif n == '4':
        return 'Победа'
    elif n == '5':
        return 'UTair'

def air_seats(n):
    if n == '1':
        return 'Эконом класс'
    if n == '2':
        return 'Бизнес класс'

def train_seats(n):
    if n == '1':
        return 'Плац-карт'
    if n == '2':
        return 'Купе'

# данные переменные дают пользователю выбор
cities = '1 - Москва, 2 - Санкт-Перебург, 3 - Екатеринбург,' \
         ' 4 - Сочи, 5 - Краснодар, 6 - Новосибирск,' \
         ' 7 - Укажите город, в который вы хотите поехать'
transport = '1 - На самолёте, 2 - На поезде, 3 - На машине, 4 - Пешком'
companies = '1 - Аэрофлот, 2 - S7, 3 - Red Wings, 4 - Победа, 5 - Utair'

# создаём список для "загрузки"
loading = ['1 ', '2 ' , '3', '.', '.', '.']

# создаём список городов, в которые может поехать пользователь
cities_list = ['Москва', 'Санкт-Перебург',
               'Екатеринбург', 'Сочи', 'Краснодар', 'Новосибирск']

# приветствие бота с клиентом
print("Здравствуйте! Добро пожаловать в ТревелГид")
'''.capitalize() метод работы со строками, 
возвращает строку таковой, что 1 буква заглавная'''
name = input('Как Вас зовут?').capitalize()

# cкладываем 2 строки через название переменной name,
# + и "", так мы будем делать много раз
print(name + ", " + 'куда поедете в этот раз?')
print("Укажите числовое значение, пожалуйста! \n" + cities)


while True:
    # создаём переменную city_ для ввода с клавиатуры
    city_ = input()
    # создаём новую переменную и пользуемся функции, написанной выше
    City_ = city(city_)
    if city_ == '1' or city_ == '2' or city_ == '3' \
            or city_== '4' or city_ == '5' or city_ == '6':
        print("Хороший выбор")
        break
    elif city_ == '7':
        city_new = input("Введите название города, "
                         "в который Вы хотите поехать:\n").capitalize()
        cities_list.append(city_new)
        break
    else:
        print(name + ", я Вас не понимаю, введите цифру от 1 до 7")

print(name + ", давайте разберёмся транспортом!\n" + transport)

# создаём цикл, для того,
# чтобы человек мог повторно выбрать цифру, если он ошибся
while True:
    # создаём переменную transport_ для ввода с клавиатуры
    transport_ = input()
    # создаём новую переменную и пользуемся фоункцие, написанной выше
    Transport_ = type_of_transport(transport_)
    # проверяем условие, если переменная транспорт равна 1
    if transport_ == '1':
        # если переменная равна 1, то выполняем условия для самолёта
        print(name + ", " + "давайте "
                            "определимся с авиакомпанией:\n" + companies)
        # создаём переменную companies_ для ввода с клавиатуры
        companies_ = input()
        # создаём новую переменную и пользуемся фоункцие, написанной выше
        Companies_ = air_company(companies_)
        print("Выбирите места в самолёте, на которых вы хотите сидеть\n"
              "1 - Эконом класс, 2 - Бизнес класс")
        '''создаём переменную air_seats_,
                которая будет относиться к функции air_seats,
                чтобы проверять, какие места выбирает пользователь'''
        # создаём переменную air_seats_ для ввода с клавиатуры
        air_seats_ = input()
        air_Seats = air_seats(air_seats)
        # Условия для проверки переменной air_seats_
        if air_seats_ == '1':
            # выводим список laoading в строку(загрузка)
            for i in range(len(loading)):
                print(loading[i], end="")
            print(name +', забронировал Вам место в эконом классе')
        elif air_seats_ == '2':
            # выводим список laoading в строку(загрузка)
            for i in range(len(loading)):
                print(loading[i], end="")
            print()
            print(name +', забронировал Вам место в бизнес классе')
        elif air_seats_ != '1' or air_seats_ != '2':
            print(name + ", я Вас не понимаю, введите пожалуйста цифру 1 или 2")
        print("Хорошей поездки и мягкой посадки!")
        # заканчиваем цикл while, потому что мы получили конечный результат
        break
    # проверяем условие, если переменная транспорт равна 2
    elif transport_ == '2':
        # если переменная равна 2, то выполянем условие для поезда
        print(name +", выбирите в каком вагоне Вы хотите ехать:\n"
                    "1 - Плацкарт, 2 - Купе")
        # создаём переменную train_seats_ для ввода с клавиатуры
        train_seats_ = int(input())
        train_Seats = train_seats(train_seats)
        if train_seats_ == '1':
            # выводим список laoading в строку(загрузка)
            for i in range(len(loading)):
                print(loading[i], end="")
            print()
            print(name +', забронировал Вам место в плацкарте')
        elif train_seats_ == '2':
            # выводим список laoading в строку(загрузка)
            for i in range(len(loading)):
                print(loading[i], end="")
            print()
            print(name +", забронировал Вам место в купе")
        print(name + ", хорошей поездки!")
        # заканчиваем цикл while, потому что мы получили конечный результат
        break
    # проверяем условие, если переменная транспорт равна 3
    elif transport_ == '3':
        '''если переменная равна 3, то выполянем условие для машины
         выводим список laoading в строку(загрузка)'''
        for i in range(len(loading)):
            print(loading[i], end="")
        print()
        print('https://arenda-car.ru/ \n' +
              name + 'на этом сайте вы можете выбрать '
                     'машину и отправиться в путешествие, ровной дороги!')
        # заканчиваем цикл while, потому что мы получили конечный результат
        break
    elif transport_ == '4':
        # если переменная равна 4, то выполянем условие для ходьбы
        print("Советую вам вопспользоваться https://yandex.ru/maps "
              "и купить себе удобные кроссовки, хорошего похода!")
        # заканчиваем цикл while, потому что мы получили конечный результат
        break
    else:
        print(name + ", я Вас не понимаю, введите пожалуйста цифру от 1 до 3")
    # не заканчиваем цикл while, потому что мы не получили конечный результат
print("\nТеперь список городов, в которые мы будем "
      "предлагать билеты увеличивается, спасибо вам за это!\n"
      "Вот новый список городов:")

'''вывыодим с помощью цикла и массива новый список городов,
    в которые можно поехать'''
for i in range(len(cities_list)):
    print(i + 1, '- ' + cities_list[i])