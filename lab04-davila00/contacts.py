# Name: Daniel Avila
# Date: 02/20/2022
# Purpose: Functions that will add, delete, modify, sort, and find contacts
#        : in a dictionary

def add_contact(contact_dict,  id, first_name, last_name):
    """Function add contacts to the contact dictionary"""
    if id in contact_dict:
        return 'error'
    else:
        contact_dict[id] = ([first_name, last_name])
        return (first_name + " " + last_name)

def modify_contact(contact_dict,  id, first_name, last_name):
    """Function modifies contact on the contact dictionary"""
    if not id in contact_dict:
        return 'error'
    else:
        contact_dict[id] = ([first_name, last_name])
        return contact_dict[id]

def delete_contact(contact_dict,  id):
    """Function deletes contact on the contact dictionary"""
    if not id in contact_dict:
        return 'error'
    else:
        del(contact_dict[id])
        return id

def sort_contacts(contact_dict):
    """Function sorts the contact dictionary"""
    return dict(sorted(contact_dict.items(), key = lambda c:(c[1][0].lower(), c[1][1].lower())))

def find_contact(contact_dict,  find):
    """Function finds contacts in the dictionary"""
    dict = {}
    if find.isdigit():
        found = int(find)
        if found in contact_dict:
            dict[found] = contact_dict[found]
    for key, value in contact_dict.items():
        if find.lower() in value[0].lower() or find.lower() in value[1].lower():
            dict[key] = value
    dict = sort_contacts(dict)
    return dict
