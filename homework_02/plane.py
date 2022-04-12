from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo: 150

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, u_cargo):
        if self.cargo + u_cargo > self.max_cargo:
            raise CargoOverload
        self.cargo += u_cargo

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
