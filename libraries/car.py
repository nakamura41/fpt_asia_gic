class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, id, name, x, y, direction, commands):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.command_index = 0
        self.initial_position = (x, y)
        self.initial_direction = direction
        self.active = True

    def get_id(self):
        return self.id

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
        if self.command_index >= len(self.commands) or not self.active:
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
