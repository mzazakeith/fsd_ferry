import os

def main_menu():

    '''
    Function that opens the main menu and allows access to the program
    '''

    #ascii art text
    print('''
 |  \/  |  / \  |_ _| \ | | |  \/  | ____| \ | | | | |
 | |\/| | / _ \  | ||  \| | | |\/| |  _| |  \| | | | |
 | |  | |/ ___ \ | || |\  | | |  | | |___| |\  | |_| |
 |_|  |_/_/   \_|___|_| \_| |_|  |_|_____|_| \_|\___/
          ''')
    #   end of ascii art text

    print("FERRY TICKETING SYSTEM \n")
    print("Gain access using the following shortcodes:" + " \n P – to Purchase Ticket \n V –to View Seating Arrangement \n Q – to Quit the system \n")
    main_short_code = input("Short code: ").lower()
    if main_short_code == "p":
        print("PURCHASING MODULE ")
        purchase()
    elif main_short_code == "v":
        print("view")
    elif main_short_code == "q":
        os.system('clear')
        exit()
    else:
        print("Short code used is not recognised")
        print("Try again")
        main_menu()

def purchase():

    """
    Function that gives access to the purchasing module allowing the user to buy either a business class or economy class ticket
    """

    print("Continue using one of the following shortcodes:" + "\n B – to purchase ticket for Business class \n E – to purchase ticket for Economy class \n M – to return to Main Menu \n")
    purchasing_short_code = input("Short code: ").lower()
    if purchasing_short_code == "b":
        print("Business class")
    elif purchasing_short_code == "e":
        print("Economy class")
    elif purchasing_short_code == "m":
        main_menu()
    else:
        print("Short code used is not recognised")
        print("Try again")

main_menu() 