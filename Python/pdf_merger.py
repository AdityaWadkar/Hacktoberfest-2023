from PyPDF2 import PdfFileMerger 
import zlib,base64
import os
p=PdfFileMerger()
for item in os.listdir():
    if item.endswith('.pdf'):
        p.append(item)
p.write("file_name.pdf")
p.close()

