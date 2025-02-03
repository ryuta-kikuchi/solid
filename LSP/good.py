from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move_forward(self):
        pass

    @abstractmethod
    def move_backward(self):
        pass

class Turnable(ABC):
    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

class Car(Movable, Turnable):
    def move_forward(self):
        print("Car: Moving forward")

    def move_backward(self):
        print("Car: Moving backward")

    def turn_left(self):
        print("Car: Turning left")

    def turn_right(self):
        print("Car: Turning right")

class Train(Movable):
    def move_forward(self):
        print("Train: Moving forward on track")

    def move_backward(self):
        print("Train: Moving backward on track")