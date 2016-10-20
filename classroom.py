import re

class ClassRoom:
    room_pattern = re.compile("^([A-Z])/([A-Z0-9])-([0-9])$")

    def __init__(self, floor, block, number, name=""):
        self.floor = floor
        self.block = block
        self.number = number
        self.name = name

ClassRoom.predefined = {
    "lab1": ClassRoom(None, None, None, "LAB1"),
    "lab2": ClassRoom(None, None, None, "LAB2"),
    "lab3": ClassRoom(None, None, None, "LAB3"),
    "elektronik lab.": ClassRoom(None, None, None, "Elektronik Lab")
}
