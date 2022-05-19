from homework_02.base import Vehicle
from homework_02.plane import Plane
from homework_02.car import Car
from homework_02.engine import Engine
from homework_02.exceptions import NotEnoughFuel


if __name__ == '__main__':
    u_vehicle = Vehicle(100, 40, 5)
    u_plane = Plane(1000, 100, 1, 100)

    u_plane.load_cargo(100)
    # u_plane.load_cargo(100)

    u_car = Car(1000, 50, 10)
    u_engine = Engine(100, 50)
    u_car.set_engine(u_engine)
    print()

    print(f'Type vehicle: {type(u_vehicle)}, \ntype plane: {type(u_plane)}, \ntype car: {type(u_car)}')
    try:
        u_vehicle.move(8)
    except NotEnoughFuel as e:
        print('NotEnoughFuel')
