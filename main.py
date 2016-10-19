#!/usr/bin/python
from docx import Document
import sys

help = '''classusage v0.0.1
   Please supply a docx file or a folder containing docx files to run this program.
   Example:
    python main.py "C:\\btbs-1.docx"
'''

if len(sys.argv) <= 1:
    print(help)
    exit()

from docparser import DocLessonParser
parser = DocLessonParser()
print(parser.parse(sys.argv[1]))
