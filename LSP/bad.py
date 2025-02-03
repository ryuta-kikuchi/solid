from abc import ABC, abstractmethod

class Vehicle:
    def move_forward(self):
        print("前移動の処理")

    def move_backward(self):
        print("後移動の処理")

    def turn_left(self):
        print("左折処理")

    def turn_right(self):
        print("右折処理")

class Car(Vehicle):
    pass

class Train(Vehicle):
    def turn_left(self):
        raise Exception("Trainは左折できません")
    
    def turn_right(self):
        raise Exception("Trainは右折できません")