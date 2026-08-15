import random


class Environment:
    def __init__(self):
        self.rooms = {
            "A": random.randint(0, 2),
            "B": random.randint(0, 2),
            "C": random.randint(0, 2),
            "D": random.randint(0, 2)
        }

        self.location = random.choice(list(self.rooms.keys()))


class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment

        self.cleaned_rooms = 0
        self.light_cleaned = 0
        self.heavy_cleaned = 0
        self.movements = 0
        self.power_used = 0
        self.score = 0

    def get_percept(self):
        return self.environment.rooms[self.environment.location]

    def choose_action(self):
        dust = self.get_percept()

        if dust == 2:
            return "DEEP CLEAN"
        elif dust == 1:
            return "CLEAN"
        else:
            return "MOVE"

    def clean_room(self, dust):
        room = self.environment.location

        if dust == 2:
            print(f"Room {room} has heavy dust.")
            print("Action: Deep Cleaning")

            self.environment.rooms[room] = 0
            self.heavy_cleaned += 1
            self.cleaned_rooms += 1
            self.power_used += 3
            self.score += 15

        else:
            print(f"Room {room} has light dust.")
            print("Action: Cleaning")

            self.environment.rooms[room] = 0
            self.light_cleaned += 1
            self.cleaned_rooms += 1
            self.power_used += 1
            self.score += 10

    def move(self):
        rooms = list(self.environment.rooms.keys())
        current = rooms.index(self.environment.location)
        next_room = (current + 1) % len(rooms)

        old_room = self.environment.location
        self.environment.location = rooms[next_room]

        self.movements += 1
        self.power_used += 1
        self.score -= 1

        print(f"Moving from Room {old_room} to Room {self.environment.location}")

    def all_clean(self):
        return all(dust == 0 for dust in self.environment.rooms.values())

    def run(self):
        print("VACUUM CLEANER")
        print("-" * 30)

        print("\nInitial Environment")

        for room, dust in self.environment.rooms.items():
            if dust == 0:
                status = "Clean"
            elif dust == 1:
                status = "Light Dust"
            else:
                status = "Heavy Dust"

            print(f"Room {room}: {status}")

        print(f"\nStarting Room: {self.environment.location}")

        step = 1

        while not self.all_clean():
            print(f"\nStep {step}")

            room = self.environment.location
            dust = self.get_percept()

            if dust == 0:
                print(f"Room {room}: Clean")
            elif dust == 1:
                print(f"Room {room}: Light Dust")
            else:
                print(f"Room {room}: Heavy Dust")

            action = self.choose_action()

            if action == "CLEAN":
                self.clean_room(dust)

            elif action == "DEEP CLEAN":
                self.clean_room(dust)

            else:
                self.move()

            step += 1

        print("\nFinal Environment")
        print("-" * 30)

        for room in self.environment.rooms:
            print(f"Room {room}: Clean")

        print("\nPerformance Report")
        print("-" * 30)
        print(f"Rooms Cleaned      : {self.cleaned_rooms}")
        print(f"Light Dust Cleaned : {self.light_cleaned}")
        print(f"Heavy Dust Cleaned : {self.heavy_cleaned}")
        print(f"Movements          : {self.movements}")
        print(f"Power Used         : {self.power_used}")
        print(f"Performance Score  : {self.score}")

        print("\nAll rooms are clean.")


environment = Environment()
vacuum = VacuumCleaner(environment)
vacuum.run()