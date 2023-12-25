# Description: Script to merge multiple pdf file using python.
# Original Author: Haim Cohen 
# https://www.linkedin.com/in/haimc/

import PyPDF2
import os

def merge_pdfs(input_folder, output_file):
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    pdf_files.sort()
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_merger.append(pdf_path)

    with open(output_file, 'wb') as output:
        pdf_merger.write(output)

if __name__ == "__main__":
    input_folder = '/path/to/pdf/files'
    output_file = '/path/to/merged/pdf/merged.pdf'
    merge_pdfs(input_folder, output_file)
    print(f"Merged PDF saved to: {output_file}")
