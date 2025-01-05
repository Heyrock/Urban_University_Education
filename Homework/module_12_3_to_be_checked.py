class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# runner = Runner('Vasya')
# print(runner.__eq__(runner))
# print(runner.__eq__('Vasya'))
# print(runner)

# usain = Runner(name='Усэйн', speed=10)
# andrey = Runner(name='Андрей', speed=9)
# nick = Runner(name='Ник', speed=3)
#
# t = Tournament(90, *[usain, andrey, nick])

# for item, value in t.start().items():
#     print(item, value)
# print({item: value.name for item, value in t.start().items()})

# print(t.start())
