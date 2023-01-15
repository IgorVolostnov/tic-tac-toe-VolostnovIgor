#Игра крестики-нолики
def hello():
    out_yellow("Привет! Это Игра Крестики-Нолики")
    out_yellow("---------Правила Игры:----------")
    out_yellow("-Это логическая игра между двумя")
    out_yellow("противниками на квадратном поле:")
    out_yellow("3 на 3 клетки. Один из игроков в")
    out_yellow("ней играет «крестиками», второй ")
    out_yellow(" — «ноликами». Чтобы сделать ход")
    out_yellow(" нужно ввести двухзначное число:")
    out_yellow("номер столбца, затем номер строки")
#Цветной текст
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
def out_black(text):
    print("\033[0m {}" .format(text))

#Вывод экрана
def output_screen(dictionary_values):
    screen = [
        ["  ", "\u0332" + "0", " ", "\u0332" + "1", " ", "\u0332" + "2", " "],
        ["0", "|", "\u0332" + field_values["00"], "|", "\u0332" + field_values["10"], "|", "\u0332" + field_values["20"], "|"],
        ["1", "|", "\u0332" + field_values["01"], "|", "\u0332" + field_values["11"], "|", "\u0332" + field_values["21"], "|"],
        ["2", "|", "\u0332" + field_values["02"], "|", "\u0332" + field_values["12"], "|", "\u0332" + field_values["22"], "|"]
        ]
    for i in range(4):
        print("".join(screen[i]))

#Проверка кто победил
def who_won(dictionary_values):
    list_values = []
    for key_, values_ in dictionary_values.items():
        list_values.append(values_)
    if any(["".join(list_values[0:3]) == "XXX",
           "".join(list_values[3:6]) == "XXX",
           "".join(list_values[6:9]) == "XXX",
           "".join(list_values[0:9:3]) == "XXX",
           "".join(list_values[1:9:3]) == "XXX",
           "".join(list_values[2:9:3]) == "XXX",
           "".join(list_values[0:9:4]) == "XXX",
           "".join(list_values[2:7:2]) == "XXX"]):
        winer = 1
    elif any(["".join(list_values[0:3]) == "000",
           "".join(list_values[3:6]) == "000",
           "".join(list_values[6:9]) == "000",
           "".join(list_values[0:9:3]) == "000",
           "".join(list_values[1:9:3]) == "000",
           "".join(list_values[2:9:3]) == "000",
           "".join(list_values[0:9:4]) == "000",
           "".join(list_values[2:7:2]) == "000"]):
        winer = 2
    else:
        winer = 0
    return winer

#Сколько полей заполнено
def end_game(dictionary_values):
    list_values = []
    for key_, values_ in dictionary_values.items():
        list_values.append(values_)
    return list_values.count(" ")

#Игра
def game():
    out_black("Игра началась")
    global field_values
    field_values = {"00": " ", "10": " ", "20": " ", "01": " ", "11": " ", "21": " ", "02": " ", "12": " ", "22": " "}
    while who_won(field_values) == 0:
        #Ход первого игрока
        output_screen(field_values)
        out_red(Walking_Now1)
        while True:
            move_player1 = input()
            if move_player1 in field_values.keys():
                if field_values[move_player1] == " ":
                    field_values[move_player1] = "X"
                    if end_game(field_values) == 0:
                        out_black("У Вас ничья!!!")
                        output_screen(field_values)
                        return "0"
                        break
                    break
                else:
                    print("Данное поле уже занято, введите другое поле")
            else:
                print("Вы ввели некорректные данные, введеите номер столбца, затем номер строки, например '12'")
        if who_won(field_values) == 1:
            out_yellow("ПОЗДРАВЛЕНИЯ!!!")
            output_screen(field_values)
            out_red(Won_Player1)
            return "1"
            break

        #Ход второго игрока
        output_screen(field_values)
        out_blue(Walking_Now2)
        while True:
            move_player2 = input()
            if move_player2 in field_values.keys():
                if field_values[move_player2] == " ":
                    field_values[move_player2] = "0"
                    if end_game(field_values) == 0:
                        out_black("У Вас ничья!!!")
                        output_screen(field_values)
                        return "0"
                        break
                    break
                else:
                    print("Данное поле уже занято, введите другое поле")
            else:
                print("Вы ввели некорректные данные, введеите номер столбца, затем номер строки, например '12'")
        if who_won(field_values) == 2:
            out_yellow("ПОЗДРАВЛЕНИЯ!!!")
            output_screen(field_values)
            out_blue(Won_Player2)
            return "2"
            break

#Процесс игры
hello()
out_red("Введите имя Игрока 1:")
NameGamer1 = input()
Walking_Now1 = "Сейчас ходит Игрок1" if NameGamer1 == "" else "Сейчас ходит " + NameGamer1
Won_Player1 = "В этот раз побеждает Игрок1" if NameGamer1 == "" else "В этот раз побеждает " + NameGamer1
out_blue("Введите имя Игрока 2:")
NameGamer2 = input()
Walking_Now2 = "Сейчас ходит Игрок2" if NameGamer2 == "" else "Сейчас ходит " + NameGamer2
Won_Player2 = "В этот раз побеждает Игрок2" if NameGamer2 == "" else "В этот раз побеждает " + NameGamer2
while True:
    game()
    while True:
        answer = input("Сыграем ещё раз? да/нет: ")
        if any([answer.lower() == "да", answer.lower() == "нет"]):
            break
        else:
            print("Не понятно, да или нет?")
    if answer.lower() == "нет":
        out_black("До скорых встреч!")
        break