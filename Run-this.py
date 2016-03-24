import PyPDF2 as pdf
import os

output = pdf.PdfFileMerger()

base_directory = str(os.getcwd())
pdf_directory = base_directory + "/pdfs/"

for file in os.listdir(pdf_directory):
    print(pdf_directory + str(file))
    output.append(pdf_directory + str(file))

output.write(base_directory + "/" + "COMBINED_PDF.pdf")