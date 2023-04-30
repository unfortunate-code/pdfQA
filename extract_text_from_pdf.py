from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    pdf_file = open(pdf_path, 'rb')

    # Create a PDF reader object
    reader = PdfReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = len(reader.pages)

    content = []

    # Loop through each page and extract the text
    for page_num in range(num_pages):
        # Get the current page
        page = reader.pages[page_num]

        # Extract the text from the page
        text = page.extract_text()

        content.append(text)

    # Close the PDF file
    pdf_file.close()
    return '\n'.join(content)