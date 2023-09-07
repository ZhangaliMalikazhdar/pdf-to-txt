from pdf2image import convert_from_path

import pytesseract
from PIL import Image

# Store Pdf with convert_from_path function
images = convert_from_path('pdfs/1.pdf')
images[0].save('pdfs/page'+'.jpg', 'JPEG')


img= Image.open("pdfs/page.jpg")
text = pytesseract.image_to_string(img, lang='rus')
print(text)