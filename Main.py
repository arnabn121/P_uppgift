import sys as sys

names_of_lists = []


def create_list():
    list_name = input("Vad ska listan heta?: ")
    while list_name.upper() not in names_of_lists:
        list_name = input(list_name + " finns redan som lista. Ange ett annat namn: ")

    names_of_lists.append(list_name)

    file = open(list_name + ".txt", "w+")
    i = 1
    print("Avsluta genom att skriva 0")
    while True:
        item = input("Föremål " + str(i) + ": ")
        if item == "0":
            break
        file.write(item + "\n")
        i += 1
    print(list_name + " listan har blivit skapad.")


def option():
    possible_choices = ["N", "I", "S", "A", "Z"]
    while True:
        print("Ditt val: ", end="")
        option = input().upper()
        if option.isnumeric() or option not in possible_choices:
            print("Felaktig input")
            continue
        break
    return option


def selected_choice(option):
    if option == "Z":
        print("Du har valt att avsluta")
        sys.exit(0)
    if option == "N":
        create_list()


print("Välkommen till Packningsprogrammet!" "\n"
      "N Ny Packlista" "\n"
      "I Visa innehåll i lista" "\n"
      "S Lägg till sak till en lista" "\n"
      "A Visa alla kommande listor" "\n"
      "Z Avsluta")


selected_choice(option())


