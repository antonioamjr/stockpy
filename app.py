import sys

def welcome_msg():
    print("Welcome to: ")
    print("  _________ __                 __     _________                                           .___             ")
    print(" /   _____//  |_  ____   ____ |  | __ \\_   ___ \\  ____   _____   _____ _____    ____    __| _/___________  ")
    print(" \\_____  \\\\   __\\/  _ \\_/ ___\\|  |/ / /    \\  \\/ /  _ \\ /     \\ /     \\__  \\\\  /    \\  / __ |/ __ \\_  __ \\ ")
    print(" /        \\|  | (  <_> )  \\___|    <  \\     \\___(  <_> )  Y Y  \\  Y Y  \\/ __ \\|   |  \\/ /_/ \\  ___/|  | \\/ ")
    print("/_______  /|__|  \\____/ \\___  >__|_ \\  \\______  /\\____/|__|_|  /__|_|  (____  /___|  /\\____ |\\___  >__|    ")
    print("        \\/                  \\/     \\/         \\/             \\/      \\/     \\/     \\/      \\/    \\/        ")
    print("\n")

def add_stocks(s_array):
    print(s_array)

def fill_file_stocks():
    try:
        with open(sys.argv[1], "r") as f:
            array = []
            for line in f:
                array.append(line.split())
            add_stocks(array)
    except FileNotFoundError:
        print("File \"{}\" not found".format(sys.argv[1]))

if __name__ == "__main__":
    welcome_msg()
    if len(sys.argv) > 1:
        fill_file_stocks()
