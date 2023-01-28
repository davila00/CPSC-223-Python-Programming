# Name: Daniel Avila
# Date: 02/04/2022
# Purpose: Functions that will print a list, and add, delete and modify contacts

import contacts

contact_list = []

while (True):
    print("\n\t\t***TUFFY TITATN CONTACT MAIN MENU***\n")

    print("a. Print list \nb. Add contact \nc. Modify contact")
    print("d. Delete contact \ne. Exit the program")
    choice = input("\nEnter Menu Choice: ")

    if choice == 'a':
        contacts.print_list(contact_list)
    elif choice == 'b':
        contact_list = contacts.add_contact(contact_list)
    elif choice == 'c':
        contact_list = contacts.modify_contact(contact_list)
    elif choice == 'd':
        contact_list = contacts.delete_contact(contact_list)
    elif choice == 'e':
        break
contacts.print_list(contact_list)
