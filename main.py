#!/usr/bin/python
import docx
import sys

help = '''classusage v0.0.1
   Please supply a docx file or a folder containing docx files to run this program.
   Example:
    python main.py "C:\\btbs-1.docx"
'''

if len(sys.argv) <= 1:
    print(help)
    exit()
