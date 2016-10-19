from lessonparser import LessonParser
from lesson import Lesson
from docx import Document
import re

class TableMeta:
    day_names = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

    def __init__(self, days):
        self.days = days

class StandartDocParser:
    time_pattern = re.compile("^([0-9]{2})\\.([0-9]{2})-([0-9]{2})\\.([0-9]{2})$")

    '''Parses a block of text to create a lesson object.
    Parameters
    ----------
    text : string
        Block of text representing a cell of a table row.
    '''
    def parseLesson(self, cell):
        return cell.text

    def getMeta(self, document):
        row = document.tables[0].rows[0]
        if row.cells[1].text.strip() in TableMeta.day_names:
            return TableMeta(list(map(lambda cell: cell.text.strip(), row.cells[1:])))
        return None

    def getLessons(self, row, meta):
        # Return empty if there are no cells.
        if len(row.cells) <= 0:
            return []

        time = self.parseTime(row.cells[0])
        if time is None:
            return []

        result = []
        # Parse lesson object for other cells
        for cell in row.cells[1:]:
            lesson = self.parseLesson(cell)

            if lesson:
                result.append(lesson);
                #result += lesson

        return result

    def parseTime(self, cell):
        # Check if the first row is the time row.
        match = StandartDocParser.time_pattern.match(cell.text.strip())
        if match is None:
            return None

        return [
            int(match.group(1)) * 60 + int(match.group(2)),
            int(match.group(3)) * 60 + int(match.group(4))
        ]

class DocLessonParser(LessonParser):
    def getSupportedExtensions(self):
        return ["docx"]

    def canParse(self, path):
        return path.endswith('docx')

    def parse(self, path):
        document = Document(path)
        parser = StandartDocParser()
        results = []

        # Parse metadata and initialize the parsing.
        # meta contains info such as days.
        meta = parser.getMeta(document);
        if meta is None:
            return None

        # Parse each row and get lessons
        for row in document.tables[0].rows:
            lessons = parser.getLessons(row, meta)
            results = Lesson.mergeLessons(results, lessons);

        return results