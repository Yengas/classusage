class Lesson:
    def __init__(self, subject, code, teacher, room):
        self.subject = subject
        self.code = code
        self.teacher = teacher
        self.room = room

    @staticmethod
    def mergeLessons(list, merges):
        return list + merges
