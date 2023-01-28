# Name: Daniel Avila
# Date: 02/20/2022
# Purpose: Functions that will add, delete, modify, sort, and find contacts

import contacts

contact_dict = {}

while (True):
    print("\n\t\t***TUFFY TITATN CONTACT MAIN MENU***\n")

    print("a. Add contact \nb. Modify contact")
    print("c. Delete contact \nd. Print contact list")
    print("e. Find contact \nf. Exit the program")
    choice = input("\nEnter Menu Choice: ")

    if choice == 'a':
        id = int(input("Enter phone number: "))
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        print("Added:", contacts.add_contact(contact_dict, id, first_name , last_name), ".")

    if choice == 'b':
        index = int(input("Enter the index number: "))
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        print("Modified: ", contacts.modify_contact(contact_dict, id, first_name, last_name), ".")

    if choice == 'c':
        index = int(input("Enter the index number: "))
        print("Deleted: ", contacts.delete_contact(contact_dict, id), ".")

    if choice == 'd':
        print("=============== CONTACT LIST =========================")
        print("Last Name        First name            Phone")
        print("===========      =================     ===============")
        for i in range(len(contact_dict)):
            print(f'{str(i):8}{contact_dict[i][0]:22}{contact_dict[i][1]:22}')

    if choice == 'e':
        search = str(input("Enter search string: "))
        contact_dict = contacts.find_contact(contact_dict, search)

    if choice == 'f':
        break

        if len(id) != 3

        if int(enter[0] != 1)

        if int(enter[2] < 3)

        leave_floor = 0
        leave_room = 1


        for floor in range(3):
            for room in range(4):
                for id in tracker[floor][room]:
                    leave_room = room
                    leave_floor = floor
        #leave_floor and leave_room to enter_floor and enter_room    
        valid_move =
        [1,0,1,1]
        [1,1,1,0]
        [1,4,2,4]
