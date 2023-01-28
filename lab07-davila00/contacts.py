import json
class Contacts(object):
    """docstring for Contacts."""

    def __init__(self, *, filename):
        super(Contacts, self).__init__()
        self.filename = filename
        self.contactDict = {}
        try:
            with open(self.filename, 'r') as file:
                self.contactDict = json.load(file)
        except FileNotFoundError:
            return {}

    def add_contact(self, *, id, first_name, last_name):
        if id in self.contactDict:
            return 'error'
        else:
            self.contactDict[id] = [first_name, last_name]
            sorted(self.contactDict)
            sorted(self.contactDict.values())
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return self.contactDict[id]

    def modify_contact(self, *, id, first_name, last_name):
        if id not in self.contactDict:
            return 'error'
        else:
            self.contactDict[id] = [first_name, last_name]
            sorted(self.contactDict)
            sorted(self.contactDict.values())
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return self.contactDict[id]

    def delete_contact(self, *, id):
        if id not in self.contactDict:
            return 'error'
        else:
            del self.contactDict[id]
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return self.contactDict
