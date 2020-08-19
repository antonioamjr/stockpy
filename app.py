import sys

# Program constants
AMOUNT = 0
PRICE = 1
GRADE = 2
total_grade = 0
total_patrimony = 0.0

def welcome_msg():
    print("Welcome to: ")
    print("  _________ __                 __     _________                                           .___             ")
    print(" /   _____//  |_  ____   ____ |  | __ \\_   ___ \\  ____   _____   _____ _____    ____    __| _/___________  ")
    print(" \\_____  \\\\   __\\/  _ \\_/ ___\\|  |/ / /    \\  \\/ /  _ \\ /     \\ /     \\__  \\\\  /    \\  / __ |/ __ \\_  __ \\ ")
    print(" /        \\|  | (  <_> )  \\___|    <  \\     \\___(  <_> )  Y Y  \\  Y Y  \\/ __ \\|   |  \\/ /_/ \\  ___/|  | \\/ ")
    print("/_______  /|__|  \\____/ \\___  >__|_ \\  \\______  /\\____/|__|_|  /__|_|  (____  /___|  /\\____ |\\___  >__|    ")
    print("        \\/                  \\/     \\/         \\/             \\/      \\/     \\/     \\/      \\/    \\/        ")
    print("\n")

def create_stocks_dict() -> dict:
    try:
        with open(sys.argv[1], "r") as f:
            global total_grade
            global total_patrimony

            stocks = {}
            total_grade = 0
            total_patrimony = 0.0

            for line in f:
                line = line.split()

                if len(line) == 0:
                    continue

                stocks[line[0]] = line[1:]
                total_patrimony += int(line[1]) * float(line[2])
                total_grade += int(line[3])
                
            return stocks
    except FileNotFoundError:
        print(f"File \"{sys.argv[1]}\" not found")


def print_decision(key, amount, price, grade, stocks_miss):
    print(f"Code: {key}, Amount: {amount}, Price: {price}, Grade: {grade}, ", end="")
    if stocks_miss > 0:
        print(f"Decision: Buy {stocks_miss}")
    else:
        print(f"Decision: Wait")
    

def portfolio_decision(stocks: dict):
    keys = list(stocks)
    global total_grade
    global total_patrimony

    print(f"Total Portfolio in currency: R$ {round(total_patrimony,2)}")
    print(f"Portfolio Size: {len(stocks)}\n")
    
    keys.sort()
    for key in keys:
        price = float(stocks[key][PRICE])
        grade = int(stocks[key][GRADE])
        amount = int(stocks[key][AMOUNT])

        target = grade / total_grade
        amount_miss = (target * total_patrimony) - (price * amount)
        stocks_miss = ((target * total_patrimony) - (price * amount)) / price

        print_decision(key, amount, price, grade, int(stocks_miss))

if __name__ == "__main__":
    welcome_msg()
    if len(sys.argv) > 1:
        stocks = create_stocks_dict()
        portfolio_decision(stocks)
