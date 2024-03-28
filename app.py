# Description: Script to merge multiple pdf file using python.
# Original Author: Haim Cohen 
# https://www.linkedin.com/in/haimc/
import PyPDF2
import os
import sys

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
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <input_folder> <output_file>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = sys.argv[2]

    # Check if input folder exists
    if not os.path.isdir(input_folder):
        print("Error: Input folder does not exist.")
        sys.exit(1)

    merge_pdfs(input_folder, output_file)
    print(f"Merged PDF saved to: {output_file}")

def test_dummy():
    pass

