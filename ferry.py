import os
import datetime as dt
from datetime import date

def main_menu():
    pm=Purchasing_module()
    sm = Seats_module()

    '''
    Function that opens the main menu and allows access to the program
    '''
    os.system('clear')
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
        pm.purchase()
    elif main_short_code == "v":
        print("SEATING ARRANGEMENT MODULE")
        sm.seats()
    elif main_short_code == "q":
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Short code used is not recognised")
        print("Try again")
        main_menu()

class Purchasing_module:
    def purchase(self):
        """
        Function that gives access to the purchasing module allowing the user to buy either a business class or economy class ticket
        """
        pm=Purchasing_module()
        print("Continue using one of the following shortcodes:" + "\n B – to purchase ticket for Business class \n E – to purchase ticket for Economy class \n M – to return to Main Menu \n")
        global purchasing_short_code
        purchasing_short_code = input("Short code: ").lower()
        if purchasing_short_code == "b":
            print("Business class")
            pm.available()
        elif purchasing_short_code == "e":
            print("Economy class")
            pm.available()
        elif purchasing_short_code == "m":
            os.system('clear')
            main_menu()
        else:
            os.system('clear')
            print("Short code used is not recognised")
            print("Try again")
            pm.purchase()

    def available(self):

        """
        Function that shows current time and ferries that have left and those that are available throughout the day
        """
        pm=Purchasing_module()
        # showing already departed ferries based on time

        print("\nThe already departed ferries are as follows: ")
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
            elif current_time == final_time:
                print("All ferries have already departed. The ferry service is currently closed the next ferry leaves at "+ str(base_time)+" am" )
                break
            elif current_time > final_time :
                print("All ferries have already departed. The ferry service is currently closed the next ferry leaves at "+ str(base_time)+" am" )
                break
            elif current_time == base_time:
                print(str(base_time)+":00 hrs ferry")
                break
            else:
                print("no ferry has left yet")
                break

        #showing available ferries based on time
        print("\nThe available ferries are as follows: ")
        while True:
            if current_time < base_time:
                print(str(base_time)+":00 hrs ferry")
                base_time = base_time + 1
                if base_time == final_time + 1:
                    break
            if current_time == base_time:
                base_time = base_time + 1
                print(str(base_time)+":00 hrs ferry")
                if base_time == final_time + 1:
                    break
            if current_time > base_time and current_time < final_time:
                base_time = current_time + 1
                print(str(base_time)+":00 hrs ferry")
                base_time = base_time + 1
                if base_time == final_time + 1:
                    break
            if current_time > final_time:
                print("There are no more available ferries today, please book for a different day")
                break
            if current_time == final_time:
                print("There are no more available ferries today, please book for a different day")
                break

        pm.booking_proceed()

    def booking_proceed(self):
        """
        Function to ask if a user wants to proceed with the seat booking opeartion
        """
        pm=Purchasing_module()
        print("\nDo you want to proceed? [Y/N/DD] (type DD to book for a different date other than today) ")
        book_proceed = input()
        book_proceed = book_proceed.lower()
        if book_proceed == "y":
            pm.continue_booking()
        elif book_proceed == "n":
            os.system('clear')
            main_menu()
        elif book_proceed == "dd":
            pm.continue_booking_d_date()
        else:
            print("Invalid response !!!")
            pm.booking_proceed()


    def continue_booking(self):
        """
        Function to allow the user to book the trip he/ she wants
        """
        pm=Purchasing_module()
        global time_of_trip
        time_of_trip = input("Please select the time for your trip in the following format HH(which is the hour) e.g 11 : ")
        global ferry_id, date
        now = dt.datetime.now()
        date = now.strftime("%Y-%m-%d")
        if time_of_trip == "10":
            ferry_id = "001"
        elif time_of_trip == "11":
            ferry_id = "002"
        elif time_of_trip == "12":
            ferry_id = "003"
        elif time_of_trip == "13" or time_of_trip == "1": 
            ferry_id = "004"
        elif time_of_trip == "14" or time_of_trip == "2":
            ferry_id = "005"
        elif time_of_trip == "15" or time_of_trip == "3":
            ferry_id = "006"
        elif time_of_trip == "16" or time_of_trip == "4":
            ferry_id = "007"
        elif time_of_trip == "17" or time_of_trip == "5":
            ferry_id = "008"
        else:
            ferry_id = "000"
        pm.place()
        

    def continue_booking_d_date(self):
        pm=Purchasing_module()
        """
        Function to allow the user to book the trip he/she wants on a different day
        """
        global date, ferry_id, time_of_trip
        date = input('Please Enter the date for your trip \nIn "YYYY-MM-DD" Format (E.g.[2018-12-04]): ')
        newdate = dt.datetime.strptime(date, "%Y-%m-%d")
        today =  dt.datetime.now()
        if today > newdate :
            print("That date has already passed please enter a date in the new future")
            pm.continue_booking_d_date()
        else:
            print('Here are our list of daily ferries\nleaves at 10:00hrs \nleaves at 11:00hrs\nleaves '
                'at 12:00hrs\nleaves at 13:00hrs\nleaves at 14:00hrs\nleaves at 15:00hrs\nleaves'
                ' at 16:00hrs\nleaves at 17:00hrs\n')
            time_of_trip = input("Please select the time for your trip in the following format HH(which is the hour) e.g 11 : ")
            if time_of_trip == "10":
                ferry_id = "001"
            elif time_of_trip == "11":
                ferry_id = "002"
            elif time_of_trip == "12":
                ferry_id = "003"
            elif time_of_trip == "1" or time_of_trip == "13":
                ferry_id = "004"
            elif time_of_trip == "2" or time_of_trip == "14":
                ferry_id = "005"
            elif time_of_trip == "3" or time_of_trip == "15":
                ferry_id = "006"
            elif time_of_trip == "4" or time_of_trip == "16":
                ferry_id = "007"
            elif time_of_trip == "5" or time_of_trip == "17":
                ferry_id = "008"
            else:
                ferry_id = "000"
            pm.place()

    def place(self):
        pm=Purchasing_module()
        """
        Function that allows the user to select ports
        """
        print("Please pick your port of departure and destination port for the trip\nA. From Penang to Langkawi\nB. From Langkawi to Penang\n")
        global selected_port
        selected_port = input("Please select option A or B: ").lower()
        if purchasing_short_code == "b":
            pm.business_seat_choice()
        elif purchasing_short_code == "e":
            pm.economy_seat_choice()
        else:
            print("Internal system error")
            pm.purchase()
        
    def business_seat_choice(self):
        """
        Function for chossing seats on business class
        """
        pm=Purchasing_module()
        file_name = time_of_trip+"B"+date+selected_port
        try:
            f = open(file_name)
            print("\n")
            print('*********************************************************************************')
            print('*\t\tBUSINESS CLASS\t\t\t\t\t\t\t*')
            print('*********************************************************************************')
            print(f.read())
            print('*********************************************************************************')
            print("\n")
            print("The seats marked one(1) are taken and those marked zero(0) are available")
            print("The Seats are Ordered from LEFT to RIGHT on row one i.e (1-5) and LEFT to RIGHT on row two i.e (6-10)\n")
            seat_number = int(input('Seat number: '))
            pm.ticket()
        except FileNotFoundError:
            
            ferry_list=[]
            for i in range(0,10):
                ferry_list.append([])
            for i in range(0,10):
                for j in range(0,5):
                    ferry_list[i].append(0)
            print("\n")
            print('*********************************************************************************')
            print('*\tFerry ID : ', ferry_id, ' \t\t\t\tDate: ',date, '\t*')
            print('*********************************************************************************')
            print('*\t\tBUSINESS CLASS\t\t\t\t\t\t\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[0][0], '\t*\t',ferry_list[0][1], '\t*\t', ferry_list[0][2], '\t*\t', ferry_list[0][3], '\t*\t', ferry_list[0][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[1][0], '\t*\t', ferry_list[1][1], '\t*\t', ferry_list[1][2], '\t*\t', ferry_list[1][3], '\t*\t', ferry_list[1][4], '\t*')
            print('*********************************************************************************')
            print("\n")
            print("The Seats are Ordered from LEFT to RIGHT on row one i.e (1-5) and LEFT to RIGHT on row two i.e (6-10)\n")
            seat_number = int(input('Seat number: '))
            global sn
            sn = seat_number
            file_name = time_of_trip+"B"+date+selected_port
            if seat_number <= 5:
                row = 0
                seat_number = seat_number - 1
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item) 
                pm.ticket()
            elif seat_number > 5 and seat_number < 11:
                row = 1
                seat_number = seat_number - 6
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)  
                pm.ticket()
            else:
                print("Invalid seat choice! Please try again")
                pm.business_seat_choice()
            
    
    def economy_seat_choice(self):
        """
        Function for choosing seats on economy class
        """
        pm=Purchasing_module()
        file_name = time_of_trip+"E"+date+selected_port
        try:
            f = open(file_name)
            print("\n")
            print('*********************************************************************************')
            print('*\t\tECONOMY CLASS\t\t\t\t\t\t\t*')
            print('*********************************************************************************')
            print(f.read())
            print('*********************************************************************************')
            print("\n")
            print("The seats marked one(1) are taken and those marked zero(0) are available")
            print("The Seats are Ordered from LEFT to RIGHT on row one e.g (11-15) and LEFT to RIGHT on row two i.e (16-20) and so on\n")
            seat_number = int(input('Seat number (11-50): '))
            pm.ticket()
        except FileNotFoundError:
            ferry_list=[]
            for i in range(0,10):
                ferry_list.append([])
            for i in range(0,10):
                for j in range(0,5):
                    ferry_list[i].append(0)

            
            print("\n")
            print('*********************************************************************************')
            print('*\tFerry ID : ', ferry_id, ' \t\t\t\tDate: ',date, '\t*')
            print('*********************************************************************************')
            print('*\t\tECONOMY CLASS\t\t\t\t\t\t\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[2][0], '\t*\t',ferry_list[2][1], '\t*\t', ferry_list[2][2], '\t*\t', ferry_list[2][3], '\t*\t', ferry_list[2][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[3][0], '\t*\t',ferry_list[3][1], '\t*\t', ferry_list[3][2], '\t*\t', ferry_list[3][3], '\t*\t', ferry_list[3][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[4][0], '\t*\t',ferry_list[4][1], '\t*\t', ferry_list[4][2], '\t*\t', ferry_list[4][3], '\t*\t', ferry_list[4][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[5][0], '\t*\t',ferry_list[5][1], '\t*\t', ferry_list[5][2], '\t*\t', ferry_list[5][3], '\t*\t', ferry_list[5][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[6][0], '\t*\t',ferry_list[6][1], '\t*\t', ferry_list[6][2], '\t*\t', ferry_list[6][3], '\t*\t', ferry_list[6][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[7][0], '\t*\t',ferry_list[7][1], '\t*\t', ferry_list[7][2], '\t*\t', ferry_list[7][3], '\t*\t', ferry_list[7][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[8][0], '\t*\t',ferry_list[8][1], '\t*\t', ferry_list[8][2], '\t*\t', ferry_list[8][3], '\t*\t', ferry_list[8][4], '\t*')
            print('*********************************************************************************')
            print('*\t', ferry_list[9][0], '\t*\t',ferry_list[9][1], '\t*\t', ferry_list[9][2], '\t*\t', ferry_list[9][3], '\t*\t', ferry_list[9][4], '\t*')
            print('*********************************************************************************')
            print("\n")
            print("The Seats are Ordered from LEFT to RIGHT on row one e.g (11-15) and LEFT to RIGHT on row two i.e (16-20) and so on\n")
            seat_number = int(input('Seat number (11-50): '))
            global sn
            sn = seat_number
            file_name = time_of_trip+"E"+date+selected_port
            if seat_number <= 15:
                row = 2
                seat_number = seat_number - 11
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)  
                pm.ticket()
            elif seat_number > 15 and seat_number < 21:
                row = 3
                seat_number = seat_number - 16
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 20 and seat_number < 26:
                row = 4
                seat_number = seat_number - 21
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 25 and seat_number < 31:
                row = 5
                seat_number = seat_number - 26
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 30 and seat_number < 36:
                row = 6
                seat_number = seat_number - 31
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 35 and seat_number < 41:
                row = 7
                seat_number = seat_number - 36
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 40 and seat_number < 46:
                row = 8
                seat_number = seat_number - 41
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            elif seat_number > 45 and seat_number < 51 :
                row = 9
                seat_number = seat_number - 46
                ferry_list[row][seat_number]=1
                with open(file_name, 'a') as myfile:
                    for item in ferry_list:
                        myfile.write("%s\n" % item)
                pm.ticket()
            else:
                print("Invalid seat choice! Please try again")
                pm.economy_seat_choice()

    def ticket(self):
        """
        Function that prints out the ticket information
        """
        print("Please enter your name for ticket procesing")
        name = input("Name: ")
        print('Name\t\t:', name)
        print('Date\t\t:', date)
        unit = ":00HRS"
        print('Time\t\t:', time_of_trip + unit)
        if selected_port == "a":
            departure = 'Penang'
            destination = 'Langkawi'
        elif selected_port == "b":
            departure = 'Langkawi' 
            destination = 'Penang'
        print('Port of departure\t:', departure)
        print('Destination port\t:', destination)
        print('Ferry ID\t:', ferry_id)
        if purchasing_short_code == "b":
            seat_class = 'Business'
        elif purchasing_short_code == "e":
            seat_class = 'Economy'
        print('Class\t\t:', seat_class)
        print('Seat number\t:',sn)

class Seats_module:
    def seats(self):
        """
        displays Seating Chart based on ferry id and ferry date
        """
        sm = Seats_module()
        print("Continue using one of the following shortcodes:" + "\n E- to select date of departure \n M – to return to Main Menu \n")
        seat_short_code = input("Short code: ").lower()
        if seat_short_code == "e":
            file_core = input("Enter the date of travel of the ferry whose arrangement you would like to view in the  format YYYY-MM-DD: ")
            file_enc = input("Enter the time of the trip 24HR format using only the hour(eg 13 for one pm)")
            port = input("Please pick your port of departure and destination port for the trip\nA. From Penang to Langkawi\nB. From Langkawi to Penang\n")
            file_root = input("What class would you like to see the arrangement of:[B/E]").upper()
            file_name = file_enc+file_root+file_core+port
            try:
                f = open(file_name)
                print("\n")
                print(f.read())
            except FileNotFoundError:
                if file_root == "B":
                    ferry_list=[]
                    for i in range(0,10):
                        ferry_list.append([])
                    for i in range(0,10):
                        for j in range(0,5):
                            ferry_list[i].append(0)
                    print('*********************************************************************************')
                    print('*\t\tBUSINESS CLASS\t\t\t\t\t\t\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[0][0], '\t*\t',ferry_list[0][1], '\t*\t', ferry_list[0][2], '\t*\t', ferry_list[0][3], '\t*\t', ferry_list[0][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[1][0], '\t*\t', ferry_list[1][1], '\t*\t', ferry_list[1][2], '\t*\t', ferry_list[1][3], '\t*\t', ferry_list[1][4], '\t*')
                    print('*********************************************************************************')
                    print("\n")
                elif file_root == "E":
                    ferry_list=[]
                    for i in range(0,10):
                        ferry_list.append([])
                    for i in range(0,10):
                        for j in range(0,5):
                            ferry_list[i].append(0)
                    print('*********************************************************************************')
                    print('*\t\tECONOMY CLASS\t\t\t\t\t\t\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[2][0], '\t*\t',ferry_list[2][1], '\t*\t', ferry_list[2][2], '\t*\t', ferry_list[2][3], '\t*\t', ferry_list[2][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[3][0], '\t*\t',ferry_list[3][1], '\t*\t', ferry_list[3][2], '\t*\t', ferry_list[3][3], '\t*\t', ferry_list[3][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[4][0], '\t*\t',ferry_list[4][1], '\t*\t', ferry_list[4][2], '\t*\t', ferry_list[4][3], '\t*\t', ferry_list[4][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[5][0], '\t*\t',ferry_list[5][1], '\t*\t', ferry_list[5][2], '\t*\t', ferry_list[5][3], '\t*\t', ferry_list[5][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[6][0], '\t*\t',ferry_list[6][1], '\t*\t', ferry_list[6][2], '\t*\t', ferry_list[6][3], '\t*\t', ferry_list[6][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[7][0], '\t*\t',ferry_list[7][1], '\t*\t', ferry_list[7][2], '\t*\t', ferry_list[7][3], '\t*\t', ferry_list[7][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[8][0], '\t*\t',ferry_list[8][1], '\t*\t', ferry_list[8][2], '\t*\t', ferry_list[8][3], '\t*\t', ferry_list[8][4], '\t*')
                    print('*********************************************************************************')
                    print('*\t', ferry_list[9][0], '\t*\t',ferry_list[9][1], '\t*\t', ferry_list[9][2], '\t*\t', ferry_list[9][3], '\t*\t', ferry_list[9][4], '\t*')
                    print('*********************************************************************************')
                    print("\n")
        elif seat_short_code == "m":
            os.system('clear')
            main_menu()
        else:
            os.system('clear')
            print("Short code used is not recognised")
            print("Try again")
            sm.seats()


main_menu()
