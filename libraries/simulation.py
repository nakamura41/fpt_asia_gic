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

    def get_car_initial_state(self):
        return [car.get_initial_state() for car in self.cars]

    def get_car_final_states(self):
        return [car.get_final_state() for car in self.cars]

    def get_collisions(self):
        return self.collisions

    def print_results(self):
        if self.collisions:
            for collision in self.collisions:
                print(f"- {collision[0]}, collides with {collision[1]} at {collision[2]} at step {collision[3]}")
        else:
            for car in self.cars:
                print(f"{car.get_final_state()}")
