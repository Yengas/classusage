import copy
import json

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
    def __init__(self, source, subject, department, code, teacher, room, optional, time):
        self.source = source
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
