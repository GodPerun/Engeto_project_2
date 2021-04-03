# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Python3 program to Split string into characters
def split(word):
    return [char for char in word]


def get_random() -> object:
    set_seznam = set("0")
    int_seznam = list(set_seznam)
    while len(set_seznam) != 4 or int_seznam[0] == 0:
        nahoda = random.randrange(1000, 9999, 1)

        seznam = split(str(nahoda))
        for i in range(0, len(seznam)):
            seznam[i] = int(seznam[i])
            set_seznam = set(seznam)
        int_seznam = list(set_seznam)
    return int_seznam


def str_to_int_list(user_input) -> object:
    """

    :rtype: object
    """
    # print(user_input)
    split_input = split(str(user_input))
    for i in range(0, len(split_input)):
        split_input[i] = int(split_input[i])

    return split_input


def count_cows_bulls(ran_cislo, zvolene_cislo):
    bulls = 0
    cows = 0
    for i, j in zip(ran_cislo, zvolene_cislo):
        if i == j:
            bulls = bulls + 1
        elif j in ran_cislo:
            cows = cows + 1
        else:
            continue
    print("bulls: ", bulls, "cows: ", cows)
    return cows


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello in Bulls&Cows game")
    print("------------------------")
    random_cislo = get_random()
    print("zadavej 4 cisla dokud neuhadnes")
    print(random_cislo)
    cows_bulls = [0, 0, 0, 0]  # 0 - nothing, 1 - a cow, 2 - a bull
    print(cows_bulls)
    while True:
        input_cislo = input(">>> ")
        try:
            int(input_cislo)
        except ValueError:
            print("Cisla musi byt 4 unikatni a nezacinat nulou")
            continue
        input_cislo = str_to_int_list(input_cislo)
        if input_cislo[0] == 0 or len(set(input_cislo)) != 4 or len(input_cislo) != 4:
            print("Cisla musi byt 4 unikatni a nezacinat nulou")
            continue
        elif random_cislo == input_cislo:
            print("vitezstvi")
            break
        else:
            bulls = 0
            cows = 0
            count_cows_bulls(random_cislo, input_cislo)
            # print(f"bulls - {bulls}, cows - {cows}....nevzdavej to")
            continue

    # if test[0] == 0 or len(set(test)) != 4:
    #     print("podminka splnena")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
