from libraries.car import Car
from libraries.simulation import Simulation


def main():
    print("Welcome to Auto Driving Car Simulation!\n")
    while True:
        width, height = map(int,
                            input("Please enter the width and height of the simulation field in x y format: ").split())
        simulation = Simulation(width, height)
        car_id = 1
        while True:
            print("Please choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            print("")
            option = int(input())
            if option == 1:
                name = input("Please enter the name of the car: ")
                x, y, direction = input(
                    f"Please enter initial position of car {name} in x y Direction format: ").split()
                x, y = int(x), int(y)
                commands = input(f"Please enter the commands for car {name}: ")
                car = Car(car_id, name, x, y, direction, commands)
                car_id += 1
                simulation.add_car(car)
                simulation.print_car_list()
            elif option == 2:
                simulation.run()
                simulation.print_car_list()
                print("After simulation, the result is:")
                simulation.print_results()
                print("")
                break
            else:
                print("Invalid option, please try again.")

        print("Please choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")
        print("")
        option = int(input())
        if option == 2:
            print("Thank you for running the simulation. Goodbye!")
            break


if __name__ == "__main__":
    main()
