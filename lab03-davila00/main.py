# Name: Daniel Avila
# Date: 02/10/2022
# Purpose: Drive the contacts module to prompt the user accordingly

import contacts

contact_list = []

while (True):
    print("\n\t\t***TUFFY TITATN CONTACT MAIN MENU***\n")

    print("a. Print list \nb. Add contact \nc. Modify contact")
    print("d. Delete contact \ne. Sort list by first name")
    print("f. Sort list by last name \ng. Exit the program")
    choice = input("\nEnter Menu Choice: ")

    if choice == 'a':
        print("=============== CONTACT LIST ===============")
        print("Index   First Name            Last Name")
        print("======  =================     ===============")
        for i in range(len(contact_list)):
            print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

    elif choice == 'b':
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        contacts.add_contact(contact_list, first_name, last_name)

    elif choice == 'c':
        index = int(input("Enter the index number: "))
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        contact_list = contacts.modify_contact(contact_list, first_name, last_name, index)
        if not contact_list:
            print("Invalid index number.")

    elif choice == 'd':
        index = int(input("Enter the index number: "))
        contact_list = contacts.delete_contact(contact_list, index)
        if not contact_list:
            print("Invalid index number.")

    elif choice == 'e':
        contact_list = contacts.sort_contacts(contact_list, 0)

    elif choice == 'f':
        contact_list = contacts.sort_contacts(contact_list, 1)

    elif choice == 'g':
        break
