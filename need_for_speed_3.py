def initial_data():
    n = int(input())
    car_data = dict()

    for i in range(n):
        data = input().split("|")
        car = data[0]
        mileage = int(data[1])
        fuel = int(data[2])
        car_data[car] = [mileage, fuel]
    while True:
        data = input().split(" : ")
        if data[0] == "Stop":
            break

        command = data[0]
        car = data[1]
        car_action(command,car,car_data,data)
    for key in car_data:
        print(f"{key} -> Mileage: {car_data[key][0]} kms, Fuel in the tank: {car_data[key][1]} lt.")

def car_action(command,car,car_data,data):
        if command == "Drive":
            distance = int(data[2])
            needed_fuel = int(data[3])
            initial_fuel = car_data[car][1]
            initial_mileage = car_data[car][0]
            if initial_fuel < needed_fuel:
                print("Not enough fuel to make that ride")
            else:
                car_data[car][0] += distance
                car_data[car][1] -= needed_fuel
                print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
                if car_data[car][0] >= 100000:
                    car_data.pop(car)
                    print(f"Time to sell the {car}!")
        if command == "Refuel":

            fuel_tank = car_data[car][1]
            fuel_to_refill = int(data[2])
            if fuel_tank + fuel_to_refill <= 75:

                car_data[car][1] += fuel_to_refill
                print(f"{car} refueled with {fuel_to_refill} liters")
            else:
                needed_fuel_to_full = 75 - fuel_tank
                car_data[car][1] += needed_fuel_to_full
                print(f"{car} refueled with {needed_fuel_to_full} liters")

        if command == "Revert":
            kilometers = int(data[2])
            initial_mileage = car_data[car][0]
            car_data[car][0] -= kilometers
            if initial_mileage > 10000:
                print(f"{car} mileage decreased by {kilometers} kilometers")
            else:
                car_data[car][0] = 10000

initial_data()