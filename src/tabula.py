# importing the necessary modules
import tabula
from tabulate import tabulate
import pandas as pd
import fitz
import io
from PIL import Image
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import pdfx



# reading the pdf
def read_pdf():
    filename=input("enter file name")
    df = tabula.read_pdf(filename, pages='1')
    print(df)

# removing the blank column
def drop_na_pdf():
    filename=input("enter file name")
    df = tabula.read_pdf(filename)
    df = df.dropna(axis='columns')
    print(df)

# extracting the particular page of a pdf
def pdf_page():
    filename=input("enter file name")
    df = tabula.read_pdf(filename, pages=3)
    print (tabulate(df))

#reading file in json format
def pdf_to_json():
    filename=input("enter file name")
    df = tabula.read_pdf(filename, pages=3, output_format="json")
    print(df) 

#reading file as a single table
def read_pdf_table():
    filename=input("enter file name")
    df = tabula.read_pdf(filename,  multiple_tables= False)
    print(df)


#reading pdf via coordinates
def read_pdf_via_coordinates():
    filename=input("enter file name")
    df = tabula.read_pdf(filename, encoding = 'ISO-8859-1',
         stream=True, area = [269.875, 12.75, 790.5, 961], pages = 4, guess = False,  pandas_options={'header':None})
    print(df)

#coverting files to csv
def pdf_to_csv():
    filename=input("enter file name")
    tabula.convert_into(filename, "output1.csv", output_format="csv", pages='all')
    print("done")

#extract images from csv
def extract_image():
    pdf_file = input("enter file name: ")

    # Input PDF file
    pdf_file = fitz.open(pdf_file)

    for page_no in range(len(pdf_file)):
        curr_page = pdf_file[page_no]
        images = curr_page.getImageList()

        for image_no, image in enumerate(curr_page.getImageList()):
            # get the XREF of the image
            xref = image[0]
            # extract the image bytes
            curr_image = pdf_file.extractImage(xref)
            img_bytes = curr_image["image"]
            # get the image extension
            img_extension = curr_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(img_bytes))
            # save it to local disk
            image.save(open(f"page{page_no+1}_img{image_no}.{img_extension}", "wb"))

#extract meta data
def extract_metadata():
    filename=input("enter file name :")
    with open(filename, "rb") as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        print(info)

#extract pages
def extract_pages():
    filename=input("enter file name: ")
    pages = convert_from_path(filename, 120)

    for page in pages:
        page.save("out.jpg", "JPEG") 

#extract URLs
def extract_url():
    filename=input("enter file name:")
# Read PDF File
    pdf = pdfx.PDFx(filename)

# Get list of URL
    print(pdf.get_references_as_dict())

#highlight words
def highlight_words():
    filename=input("enter file name: ")
    pdf_file = fitz.open(filename)

    for page in pdf_file:
        text = "<sample_text_to_highlight>"
        match_words = page.searchFor(text)

        for word in match_words:
            highlight = page.addHighlightAnnot(word)
            highlight.update()

    pdf_file.save("output.pdf")



if __name__ == '__main__':
    read_pdf()
