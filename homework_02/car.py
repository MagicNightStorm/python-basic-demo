from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = Engine(0, 0)

    def set_engine(self, value):
        self.engine = value
