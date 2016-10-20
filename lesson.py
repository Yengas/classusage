class LessonTime:
    def __init__(self, day, start, end):
        self.day = day
        self.start = start
        self.end = end

class Lesson:
    '''
    Parameters
    ----------
    optional : int
        A number representing the obligation of the lesson.
        0 means required, 1 means department wide selective, 2 means college wide selective.
    time : LessonTime
    '''
    def __init__(self, subject, department, code, teacher, room, optional, time):
        self.subject = subject
        self.department = department
        self.code = code
        self.teacher = teacher
        self.room = room
        self.optional = optional
        self.time = time

    @staticmethod
    def mergeLessons(list, merges):
        return list + merges

    def __str__(self):
        return '''
            Subject: `%s`, (%s %s)
            Teacher: `%s`
            Room(Floor: %s, Block: %s, Number: %s, Name: `%s`)
            Time: %d - %d - %d
            Optional: %d
        ''' % (self.subject, self.department, self.code, self.teacher, self.room.floor, self.room.block, self.room.number, self.room.name, self.time.day, self.time.start, self.time.end, self.optional)