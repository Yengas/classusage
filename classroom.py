import re

class ClassRoom:
    lesson_pattern = re.compile("^([A-Z])/([0-9])-([0-9])$")
    predefined = {}

    def __init__(self, floor, block, number, name=""):
        self.floor = floor
        self.block = block
        self.number = number
        self.name = name

    @staticmethod
    def parseText(text):
        text = text.strip()
        if text in ClassRoom.predefined:
            return ClassRoom.predefined[text]

        match = ClassRoom.lesson_pattern.match(text)
        if match:
            return ClassRoom(int(match.group(2)), match.group(1), (match.group(3)));

        return None
