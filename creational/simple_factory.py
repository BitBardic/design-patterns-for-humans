"""
simple factory implementation
"""
from abc import ABC, abstractmethod


class Door(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass


class WoodenDoor(Door):

    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class DoorFactory:

    @staticmethod
    def make_door(width, height):
        return WoodenDoor(width, height)


if __name__ == '__main__':
    door = DoorFactory.make_door(10, 10)
    print(door.get_height())
    print(door.get_width())
