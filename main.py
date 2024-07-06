class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.command_index = 0
        self.initial_position = (x, y)
        self.initial_direction = direction

    def rotate_left(self):
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index - 1) % 4]

    def rotate_right(self):
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index + 1) % 4]

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def execute_command(self):
        if self.command_index >= len(self.commands):
            return

        command = self.commands[self.command_index]
        self.command_index += 1

        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward()

    def get_position(self):
        return self.x, self.y

    def get_direction(self):
        return self.direction

    def has_more_commands(self):
        return self.command_index < len(self.commands)

    def get_initial_state(self):
        return f"{self.name}, ({self.initial_position[0]},{self.initial_position[1]}) {self.initial_direction}, {self.commands}"

    def get_final_state(self):
        return f"{self.name}, ({self.get_position()[0]},{self.get_position()[1]}) {self.get_direction()}"


class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []
        self.collisions = []

    def add_car(self, car):
        self.cars.append(car)

    def run(self):
        steps = 0
        while any(car.has_more_commands() for car in self.cars):
            for car in self.cars:
                if car.has_more_commands():
                    car.execute_command()
                    if not self.is_within_bounds(car):
                        continue
                    if self.check_collisions(steps):
                        return
            steps += 1

    def is_within_bounds(self, car):
        x, y = car.get_position()
        return 0 <= x < self.width and 0 <= y < self.height

    def check_collisions(self, step):
        positions = {}
        for car in self.cars:
            pos = car.get_position()
            if pos in positions:
                other_car = positions[pos]
                self.collisions.append((car.name, other_car.name, pos, step + 1))
                self.collisions.append((other_car.name, car.name, pos, step + 1))
                return True
            positions[pos] = car
        return False

    def print_car_list(self):
        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car.get_initial_state()}")
        print()

    def print_results(self):
        if self.collisions:
            for collision in self.collisions:
                print(f"- {collision[0]}, collides with {collision[1]} at {collision[2]} at step {collision[3]}")
        else:
            for car in self.cars:
                print(f"{car.get_final_state()}")


def main():
    while True:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = map(int,
                            input("Please enter the width and height of the simulation field in x y format: ").split())
        simulation = Simulation(width, height)
        while True:
            print("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation")
            option = int(input())
            if option == 1:
                name = input("Please enter the name of the car: ")
                x, y, direction = input(
                    f"Please enter initial position of car {name} in x y Direction format: ").split()
                x, y = int(x), int(y)
                commands = input(f"Please enter the commands for car {name}: ")
                car = Car(name, x, y, direction, commands)
                simulation.add_car(car)
                simulation.print_car_list()
            elif option == 2:
                simulation.run()
                simulation.print_car_list()
                print("After simulation, the result is:")
                simulation.print_results()
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
