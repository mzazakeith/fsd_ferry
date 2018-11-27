import os
import datetime as dt

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
        print("SEATING ARRANGEMENT MODULE")
        seats()
    elif main_short_code == "q":
        os.system('clear')
        exit()
    else:
        os.system('clear')
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
        available()
    elif purchasing_short_code == "e":
        print("Economy class")
    elif purchasing_short_code == "m":
        os.system('clear')
        main_menu()
    else:
        os.system('clear')
        print("Short code used is not recognised")
        print("Try again")
        purchase()

def seats():

    """
    displays Seating Chart based on ferry id and fery time
    """

    print("Continue using one of the following shortcodes:" + "\n F- to select Ferry ID \n T- to select Trip Time \n M – to return to Main Menu \n")
    seat_short_code = input("Short code: ").lower()
    if seat_short_code == "f":
        print("Enter the Ferry ID")
    elif seat_short_code == "e":
        print("Select trip time")
    elif seat_short_code == "m":
        os.system('clear')
        main_menu()
    else:
        os.system('clear')
        print("Short code used is not recognised")
        print("Try again")
        seats()

def available():

    """
    Function that shows current time and ferries that have left and those that are available throughout the day
    """
    print("The time is now :")
    
    # Getting the current time in the 12 hour system

    current_hour=dt.datetime.now().hour
    current_minute=str(dt.datetime.now().minute)
    if current_hour > 12:
        current_hour_formatted = str(current_hour - 12) 
        print(current_hour_formatted+":"+current_minute+" pm")
    elif current_hour == 12:
        print(current_hour + " noon")
    else:
        print(current_hour +":"+current_minute+"am")
    
    # showing already departed ferries based on time

    print("The already departed ferries are as follows: ")
    base_time = 10
    final_time = 17
    current_time = dt.datetime.now().hour

    while True: 
        if current_time > base_time and current_time < final_time:
            print(str(base_time)+":00 hrs ferry") 
            base_time = base_time + 1
            print(str(base_time)+":00 hrs ferry")
            if base_time == final_time:
                break 
            break
        elif current_time > final_time :
            print("The ferry service is currently closed the next ferry leaves at "+ str(base_time)+" am" )
            break
        else:
            print("no ferry has left yet")
            break

    #showing available ferries based on time
    


main_menu()

# person’s name,
# seat number, whether it is in the business or economy class of the ferry, Date and
# time of departure, Source and Destination of the trip and Ferry ID.

# Assume the company has at least 8 ferries - each with a
# different Ferry ID, which travel at one-hour intervals from 10 am to 5 pm daily.


