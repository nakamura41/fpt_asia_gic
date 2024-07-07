from enum import Enum


class State(Enum):
    ACTIVE = 1
    OUT_OF_BOUND = 2
    COLLIDED = 3
    INACTIVE = 4


class Command(Enum):
    LEFT = "L"
    RIGHT = "R"
    FRONT = "F"


class Direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

class Car:
    DIRECTIONS = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

    def __init__(self, id, name, x, y, direction, commands):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.direction = Direction(direction)
        self.commands = commands
        self.command_index = 0
        self.initial_position = (x, y)
        self.initial_direction = direction
        self.state = State.ACTIVE

    def get_id(self):
        return self.id

    def rotate_left(self):
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index - 1) % 4]

    def rotate_right(self):
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index + 1) % 4]

    def move_forward(self):
        if self.direction == Direction.NORTH:
            self.y += 1
        elif self.direction == Direction.EAST:
            self.x += 1
        elif self.direction == Direction.SOUTH:
            self.y -= 1
        elif self.direction == Direction.WEST:
            self.x -= 1

    def execute_command(self):
        if self.command_index >= len(self.commands) or self.state != State.ACTIVE:
            return

        command = self.commands[self.command_index]
        self.command_index += 1

        if command == Command.LEFT.value:
            self.rotate_left()
        elif command == Command.RIGHT.value:
            self.rotate_right()
        elif command == Command.FRONT.value:
            self.move_forward()

    def get_position(self):
        return self.x, self.y

    def get_direction(self):
        return self.direction.value

    def has_more_commands(self):
        return self.command_index < len(self.commands)

    def get_initial_state(self):
        return f"{self.name}, ({self.initial_position[0]},{self.initial_position[1]}) {self.initial_direction}, {self.commands}"

    def get_final_state(self):
        return f"{self.name}, ({self.get_position()[0]},{self.get_position()[1]}) {self.get_direction()}"

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
