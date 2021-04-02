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


def get_random():
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello in Bulls&Cows game")
    print("------------------------")
    random_cislo = get_random()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
