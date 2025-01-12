class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'make: {self.make}; model: {self.model}'


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'{super().get_info()}; fuel type: {self.fuel_type}'

vhcl = Vehicle('BMW', 'IX')
print(vhcl.get_info())
cr = Car('Tesla', 'Model S Plaid', 'Electricity')
print(cr.get_info())