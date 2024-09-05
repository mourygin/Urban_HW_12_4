class Runner:
    def __init__(self, name, speed=5):
        if type(name) == str:
            self.name = name
        else:
            raise Exception('Incorrect data type for "name" attribute.')
        self.distance = 0
        if speed >= 0:
            self.speed = speed
        else:
            raise Exception('Incorrect speed value.')


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
        min_speed = self.participants[0].speed
        turtle = self.participants[0].name
        for i in self.participants:
            if i.speed < min_speed:
                min_speed = i.speed
                turtle = i.name
        self.turtle = turtle # Прогнозируемый аутсайдер


    def start(self):
        finishers = {}
        place = 1
        # print('self.participants =', self.participants)
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers