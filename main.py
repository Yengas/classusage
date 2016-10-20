#!/usr/bin/python
from docx import Document
import sys
import os

help = '''classusage v0.0.1
   Please supply a docx file or a folder containing docx files to run this program.
   Example:
    python main.py "C:\\btbs-1.docx"
'''

if len(sys.argv) <= 1 or (not os.path.isfile(sys.argv[1]) and not os.path.isdir(sys.argv[1])):
    print(help)
    exit()

from docparser import DocLessonParser

files = []
if os.path.isfile(sys.argv[1]):
    files = [ sys.argv[1] ]
else:
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            files.append(os.path.join(dirname, filename))

parser = DocLessonParser()

for file in files:
    print("#%s" % file)
    lessons = parser.parse(file)

    for lesson in lessons:
        print(lesson)
        print("----")

    print(len(lessons))
