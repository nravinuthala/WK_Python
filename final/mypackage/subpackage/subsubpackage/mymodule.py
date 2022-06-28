
def show_menu():
    option = int(input("Press 1 for normal calculator: \n"
                      "Press 2 for scientific calculator: "))

    match option:
        case 1:
            calculator()
        case 2:
            s_calculator()

def calculator():
    print('Welcome to the calculator')

def s_calculator():
    print("Welcome to the scientific calculator.")