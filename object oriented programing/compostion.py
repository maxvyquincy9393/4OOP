class Engine:
    def start(self):
        print("brommmm")

class car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

mobil = car()
mobil.start()