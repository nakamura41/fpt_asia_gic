import unittest

from libraries.car import Car
from libraries.simulation import Simulation


class CarSimulationCase(unittest.TestCase):
    scenarios_config = [
        {
            "title": "Scenario 1: Single Car Inside the Field Boundary",
            "field": {"width": 10, "height": 10},
            "cars": [
                {"id": 1, "name": "A", "x": 1, "y": 2, "direction": "N", "commands": "FFRFFFFRRL"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,4) S'
                ],
                "collisions": []
            }
        },
        {
            "title": "Scenario 2: Two-Car Collision Within the Field Boundary",
            "field": {"width": 10, "height": 10},
            "cars": [
                {"id": 1, "name": "A", "x": 1, "y": 2, "direction": "N", "commands": "FFRFFFFRRL"},
                {"id": 2, "name": "B", "x": 7, "y": 8, "direction": "W", "commands": "FFLFFFFFFF"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,4) E',
                    'B, (5,4) S'
                ],
                "collisions": [
                    ('A', 'B', (5, 4), 7),
                    ('B', 'A', (5, 4), 7)
                ]
            }
        },
        {
            "title": "Scenario 3: Single Car Outside the Field Boundary",
            "field": {"width": 4, "height": 4},
            "cars": [
                {"id": 1, "name": "A", "x": 4, "y": 2, "direction": "N", "commands": "FFRFFFFRRL"}
            ],
            "expected": {
                "car_final_states": [],
                "collisions": []
            }
        },
        {
            "title": "Scenario 4: Three Cars with an Initial Collision",
            "field": {"width": 7, "height": 7},
            "cars": [
                {"id": 1, "name": "A", "x": 3, "y": 1, "direction": "E", "commands": "FFLFLFLFFF"},
                {"id": 2, "name": "B", "x": 2, "y": 4, "direction": "S", "commands": "FLFFLFFRFF"},
                {"id": 3, "name": "C", "x": 6, "y": 2, "direction": "W", "commands": "FLFRFFRFFL"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,1) N',
                    'B, (6,5) E',
                    'C, (5,1) S'
                ],
                "collisions": [
                    ('A', 'C', (5, 1), 3),
                    ('C', 'A', (5, 1), 3)
                ]
            }
        },
        {
            "title": "Scenario 5: Three Cars with Sequential Collisions",
            "field": {"width": 7, "height": 7},
            "cars": [
                {"id": 1, "name": "A", "x": 3, "y": 1, "direction": "E", "commands": "FFLFLFLFFF"},
                {"id": 2, "name": "B", "x": 2, "y": 4, "direction": "S", "commands": "FLFFFRFFFF"},
                {"id": 3, "name": "C", "x": 6, "y": 2, "direction": "W", "commands": "FLFRFFRFFL"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,1) N',
                    'B, (5,1) S',
                    'C, (5,1) S'
                ],
                "collisions": [
                    ('A', 'C', (5, 1), 3),
                    ('C', 'A', (5, 1), 3),
                    ('B', 'C', (5, 1), 8),
                    ('C', 'B', (5, 1), 8),
                    ('B', 'A', (5, 1), 8),
                    ('A', 'B', (5, 1), 8),
                ]
            }
        },
        {
            "title": "Scenario 6: Three Cars, Ending Out of Bounds",
            "field": {"width": 6, "height": 6},
            "cars": [
                {"id": 1, "name": "A", "x": 3, "y": 1, "direction": "E", "commands": "FFLFLFLFFF"},
                {"id": 2, "name": "B", "x": 2, "y": 4, "direction": "S", "commands": "FLFFFRFFFF"},
                {"id": 3, "name": "C", "x": 6, "y": 2, "direction": "W", "commands": "FLFRFFRFFL"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (4,-1) S',
                    'B, (5,-1) S'
                ],
                "collisions": []
            }
        }
    ]

    def parse_car(self, car_config):
        return Car(id=car_config["id"],
                   name=car_config["name"],
                   x=car_config["x"], y=car_config["y"],
                   direction=car_config["direction"],
                   commands=car_config["commands"])

    def parse_scenario(self, scenario_config):
        # initialize simulation
        simulation = Simulation(width=scenario_config["field"]["width"], height=scenario_config["field"]["height"])

        # add cars
        cars_config = scenario_config["cars"]
        for car_config in cars_config:
            car = self.parse_car(car_config)
            simulation.add_car(car)

        simulation.run()

        print(scenario_config["title"])
        print('----------------------------------------------------------------------')

        actual_collisions = simulation.get_collisions()
        expected_collisions = set(scenario_config["expected"]["collisions"])
        print(f"Comparing actual_collissions: {actual_collisions} with expected_collisions: {expected_collisions}")

        self.assertSetEqual(actual_collisions, expected_collisions)

        actual_car_final_states = simulation.get_car_final_states()
        expected_car_final_states = set(scenario_config["expected"]["car_final_states"])
        print(
            f"Comparing actual_car_final_states: {actual_car_final_states} with expected_car_final_states: {expected_car_final_states}")
        self.assertSetEqual(actual_car_final_states, expected_car_final_states)

    def test_scenarios(self):
        for scenario_config in self.scenarios_config:
            self.parse_scenario(scenario_config=scenario_config)
            print('\n')


if __name__ == '__main__':
    unittest.main()
