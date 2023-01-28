import json

class Inventory(object):
    """Inventory class and its class members"""

    def __init__(self, *, filename):
        super(Inventory, self).__init__()
        self.filename = filename
        self.data = {}
        self.qty = 0
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def add_item(self, *, barcode, description):
        if type(barcode) is not str:
            return 109
        elif barcode in self.data:
            return 101
        else:
            self.data[barcode] = [description, self.qty]
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return 100

    def modify_description(self, *, barcode, description):
        if barcode not in self.data:
            return 102
        else:
            self.data[barcode] = [description, self.qty]
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return 100

    def add_qty(self, *, barcode, qty):
        if barcode not in self.data:
            return 102
        elif type(qty) is not int:
            return 108
        else:
            self.data.update({barcode: self.qty + qty})
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return 100

    def remove_qty(self, *, barcode, qty):
        if barcode not in self.data:
            return 102
        elif type(qty) is not int:
            return 108
        elif qty > self.qty:
            return 103
        else:
            self.data.update({barcode: self.qty - qty})
            with open(self.filename, 'w') as file:
                json.dump(self.filename, file)
        return 100

    def get_inventory(self):
        pass
