from libraries.car import State

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []
        self.collisions = []

    def add_car(self, car):
        if self.is_within_bounds(car):
            self.cars.append(car)
            return True
        else:
            return False

    def run(self):
        steps = 0
        while any(car.has_more_commands() and car.get_state() == State.ACTIVE for car in self.cars):
            for car in self.cars:
                if car.has_more_commands() and car.get_state() == State.ACTIVE:
                    car.execute_command()
                    if not self.is_within_bounds(car):
                        car.set_state(State.OUT_OF_BOUND)
                        continue
                    if self.check_collisions(steps):
                        return
            steps += 1

    def is_within_bounds(self, car):
        x, y = car.get_position()
        return 0 <= x < self.width and 0 <= y < self.height

    def get_other_car_positions(self, current_car):
        positions = {}
        for car in self.cars:
            if current_car.get_id() != car.get_id():
                pos = car.get_position()
                if pos not in positions:
                    positions[pos] = []
                positions[pos].append(car)
        return positions

    def check_collisions(self, step):
        for car in self.cars:
            if car.state != State.ACTIVE:
                continue
            pos = car.get_position()
            other_car_positions = self.get_other_car_positions(car)
            if pos in other_car_positions:
                other_cars = other_car_positions[pos]
                for other_car in other_cars:
                    self.collisions.append((car.name, other_car.name, pos, step + 1))
                    self.collisions.append((other_car.name, car.name, pos, step + 1))
                    car.set_state(State.COLLIDED)
                    other_car.set_state(State.COLLIDED)

    def print_car_list(self):
        if len(self.cars) > 0:
            print("Your current list of cars are:")
            for car in self.cars:
                print(f"- {car.get_initial_state()}")
        print()

    def get_car_initial_state(self):
        return [car.get_initial_state() for car in self.cars]

    def get_car_final_states(self):
        return set([car.get_final_state() for car in self.cars])

    def get_collisions(self):
        return set(self.collisions)

    def print_results(self):
        if self.collisions:
            for collision in self.collisions:
                car_1 = collision[0]
                car_2 = collision[1]
                pos = f"({collision[2][0]},{collision[2][1]})"
                step = collision[3]
                print(f"- {car_1}, collides with {car_2} at {pos} at step {step}")
        for car in self.cars:
            if car.get_state() in (State.ACTIVE, State.OUT_OF_BOUND):
                print(f"- {car.get_final_state()}")
