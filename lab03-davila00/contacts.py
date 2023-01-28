# Name: Daniel Avila
# Date: 02/10/2022
# Purpose: Functions that will print, add, delete, modify, and sort contacts

def add_contact(contact_list, *, first_name, last_name):
    """Function add contacts to the contact list"""
    contact_list.append([first_name, last_name])

def modify_contact(contact_list, *,first_name, last_name, index):
    """Function modifies contact on the contact list"""
    if index in range(len(contact_list)):
        contact_list[index] = [first_name, last_name]
        return True
    else:
        return False

def delete_contact(contact_list, index):
    """Function deletes contact on the contact list"""
    if index in range(len(contact_list)):
        del(contact_list[index])
        return True
    else:
        return False

def sort_contacts(contact_list, column):
    """Function sorts the contact list"""
    contact_list.sort(key = lambda contact: contact[column])
