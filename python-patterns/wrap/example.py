class Engine():
    def start(self):
        return 'Start Engine'


class Car:
    def __init__(self):
        self.motor = Engine()

    def start(self):
        return self.motor.start()

if __name__ == '__main__':
    ferrari = Car()

    print(ferrari.start())