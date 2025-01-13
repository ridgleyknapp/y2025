## python3 -m pip install "pdfplumber"
import pdfplumber

import pdfplumber
pdf = pdfplumber.open("June 2021 AP-NORC PUF codebook.pdf")
page = pdf.pages[4]
page.extract_table()