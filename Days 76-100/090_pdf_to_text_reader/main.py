import PyPDF2

reader = PyPDF2.PdfReader('C:/Users/Jared/Downloads/Taming Survey.pdf')

print(len(reader.pages))

print(reader.pages[0].extract_text())
