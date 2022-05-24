from main import ParkingLot, Car

parking_lot = ParkingLot()

cars = [
    Car('KA-01-HH-1234', 21),
    Car('PB-01-HH-1234', 21),
    Car('PB-01-TG-2341', 40),
    Car('HR-29-TG-3098', 39)
]

assert parking_lot.create_parking_lot(6) is True

for i in range(0, 2):
    assert parking_lot.park(cars[i]) == i + 1

assert parking_lot.slot_numbers_for_driver_of_age(21) == [1, 2]

assert parking_lot.park(cars[2]) == 3

assert parking_lot.slot_number_for_registration_number('PB-01-HH-1234') == 2

assert parking_lot.registration_numbers_for_drivers_with_age(21) == ['KA-01-HH-1234', 'PB-01-HH-1234']

assert parking_lot.leave(2) is True
assert parking_lot.status() is True

assert parking_lot.park(cars[3]) == 2


assert parking_lot.registration_numbers_for_drivers_with_age(18) == []

assert parking_lot.slot_number_for_registration_number('MH-04-AY-1111') is None