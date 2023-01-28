# Name: Daniel Avila
# Date: 02/04/2022
# Purpose: Functions that will print a list, and add, delete and modify contacts

def print_list(contact_list):
    """Function prints the contact list"""
    print("=============== CONTACT LIST ===============")
    print("Index   First Name            Last Name")
    print("======  =================     ===============")
    for i in range(len(contact_list)):
        print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

def add_contact(contact_list):
    """Function add contacts to the contact list"""
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    contact_list.append([first_name, last_name])
    return contact_list

def modify_contact(contact_list):
    """Function modifies contact on the contact list"""
    index = int(input("Enter the index number: "))
    if index in range(len(contact_list)):
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        contact_list[index] = [first_name, last_name]
    else:
        print("Invalid index number.")
    return contact_list

def delete_contact(contact_list):
    """Function deletes contact on the contact list"""
    index = int(input("Enter the index number: "))
    if index in range(len(contact_list)):
        del(contact_list[index])
    else:
        print("Invalid index number.")
    return contact_list
