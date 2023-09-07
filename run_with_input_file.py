import sys
from pdf2image import convert_from_path

import pytesseract
from PIL import Image

pdf_name = str(sys.argv[1])

# Store Pdf with convert_from_path function
images = convert_from_path(f'pdfs/{pdf_name}')
images[0].save('pdfs/page.jpg', 'JPEG')


text = pytesseract.image_to_string(Image.open("pdfs/page.jpg"), lang='rus')
print(text)
