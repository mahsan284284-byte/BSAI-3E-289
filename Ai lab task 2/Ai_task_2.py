class TemperatureController:
    def __init__(self):
        self.previous_mode = None

    def control(self, temperature, occupied):
        previous = self.previous_mode

        if not occupied:
            target_mode = "Off"
        elif temperature < 18:
            target_mode = "Heating"
        elif temperature > 28:
            target_mode = "Cooling"
        else:
            target_mode = "Off"

        if target_mode != self.previous_mode:
            command = "Send command"
            self.previous_mode = target_mode
        else:
            command = "No command"

        return previous, target_mode, command


controller = TemperatureController()

percepts = [
    (16, True),
    (16, True),
    (18, True),
    (28, True),
    (30, True),
    (30, True),
    (22, False),
    (22, False)
]

for temperature, occupied in percepts:
    previous, target, command = controller.control(
        temperature, occupied
    )

    print(
        f"Previous Mode: {previous}, "
        f"Percept: (Temperature={temperature}°C, "
        f"Occupied={occupied}), "
        f"Target: {target}, "
        f"Outcome: {command}"
    )

