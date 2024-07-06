import unittest

from libraries.car import Car
from libraries.simulation import Simulation


class CarSimulationCase(unittest.TestCase):
    scenarios_config = [
        {
            "field": {"width": 10, "height": 10},
            "cars": [
                {"name": "A", "x": 1, "y": 2, "direction": "N", "commands": "FFRFFFFRRL"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,4) S'
                ],
                "collisions": []
            }
        },
        {
            "field": {"width": 10, "height": 10},
            "cars": [
                {"name": "A", "x": 1, "y": 2, "direction": "N", "commands": "FFRFFFFRRL"},
                {"name": "B", "x": 7, "y": 8, "direction": "W", "commands": "FFLFFFFFFF"}
            ],
            "expected": {
                "car_final_states": [
                    'A, (5,4) E',
                    'B, (5,4) S'
                ],
                "collisions": [
                    ('B', 'A', (5, 4), 7),
                    ('A', 'B', (5, 4), 7)
                ]
            }
        }
    ]

    def parse_car(self, car_config):
        return Car(name=car_config["name"], x=car_config["x"], y=car_config["y"], direction=car_config["direction"],
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

        actual_collisions = simulation.get_collisions()
        expected_collisions = scenario_config["expected"]["collisions"]
        assert actual_collisions == expected_collisions

        actual_car_final_states = simulation.get_car_final_states()
        expected_car_final_states = scenario_config["expected"]["car_final_states"]
        assert actual_car_final_states == expected_car_final_states

    def test_scenarios(self):
        for scenario_config in self.scenarios_config:
            self.parse_scenario(scenario_config=scenario_config)


if __name__ == '__main__':
    unittest.main()
