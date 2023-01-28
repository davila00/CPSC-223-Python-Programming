import sqlite3

class Contacts(object):
    """docstring for Contacts. """
    def __init__(self):
        self.databaseFile = " "

    def set_database_name(self, dbFile):
        self.databaseFile = dbFile

        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE if not exists contacts(
            contact_id INTEGER NOT NULL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
            )
        ''')
        cur.execute('''
            CREATE TABLE if not exists phones(
            phone_id INTEGER NOT NULL PRIMARY KEY,
            contact_id INTEGER NOT NULL,
            phone_type TEXT NOT NULL,
            phone_number TEXT NOT NULL
            )
        ''')
        con.commit()

    def get_database_name(self):
        return self.databaseFile

    def add_contact(self, fname, lname):
        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''INSERT INTO contacts(first_name, last_name)
            VALUES(?, ?);''', (fname, lname))
        con.commit()

    def modify_contact(self, cID, fname, lname):
        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''
            UPDATE contacts SET first_name = ?, last_name = ?
            WHERE contact_id = ?''', (fname, lname, cID))
        con.commit()

    def add_phone(self, cID, ptype, pnumber):
        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''
             INSERT INTO phones(contact_id, phone_type, phone_number)
             VALUES(?, ?, ?);''', (cID, ptype, pnumber))
        con.commit()

    def modify_phone(self, pID, ptype, pnumber):
        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''
            UPDATE phones SET phone_type = ?, phone_number = ?
            WHERE phone_id = ?''', (ptype, pnumber, pID))
        con.commit()

    def get_contact_phone_list(self):
        con = sqlite3.connect(self.databaseFile)
        cur = con.cursor()
        cur.execute('''
            SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones
            ON contacts.contact_id = phones.contact_id
            ''')
        return cur.fetchall()
        con.commit()
