
import sys
import os
from pdf2docx import Converter


pdf_path =sys.argv[1]

output_path = os.path.splitext(pdf_path)[0]+'.docx'
# docx_file = 'sampletext4.docx'

# convert pdf to docx
obj = Converter(pdf_path)
obj.convert(output_path)
obj.close()