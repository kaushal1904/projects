# Python application ~ OCR reading text from a pdf file v1.0
#-----------------------------------------------------------------------------------------------------------------------

# Readme file for more details
# Feel free to use the code
# Mentions and donations will be appreciated
# Reach out via GitHub or Email for any communication
#-----------------------------------------------------------------------------------------------------------------------

# Author: Kaushal Shastry
# Email: kaushal.shastry@outlook.com // kaushal19.shastry@gmail.com
# LinkedIn: www.linkedin.com/in/kaushal-shastry/
# PayPal: kaushal.shastry@outlook.com
#-----------------------------------------------------------------------------------------------------------------------

import numpy as np                                                      #Library for numpyarray capabilities 
from pdf2image import convert_from_path, pdf2image                      #Library to convert pdf into image
import cv2                                                              #Library for computer vision capabilitites
import pytesseract                                                      #Library for OCR capabilities
from PIL import Image                                                   #Library to open image files
import tkinter as tk                                                    #Library for using tkinter's gui capabilities
from tkinter import filedialog, messagebox                              #Library for using tkinter's gui capabilities


pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'      #executable for base binaries of pytesseract OCR, required for OCR related functions


#function to convert the uploaded pdf to text using computer vision and pytesseract OCR
def pdf_ocr(filename):

    pdf_to_img = pdf2image.convert_from_path(filename, 200, 'resources', output_file='qw')  #convert the pdf into a ppm image format file

    ppm_image = Image.open('resources/qw0001-1.ppm')

    img = cv2.cvtColor(np.asarray(ppm_image), cv2.COLOR_RGB2BGR)                             #convert the ppm image into readable image file

    cv2.imwrite("resources/output_image.jpg", img)                                           #generate a jpg file from the PPM image

    #converts the image to text in string format, set the language as required
    #Languages supported by pytesseract -> https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

    converted_text = pytesseract.image_to_string(img,lang='eng')                             #converted_text has the OCR converted text, parse it according to your needs 

    messagebox.showinfo("Information",converted_text)


#function to upload a pdf file using TKinter gui
def UploadAction(event=None):

    file = filedialog.askopenfilename()
    #print('Selected:', filename)                       #prints the name of the uploaded file
    if file:
        pdf_ocr(file)


root = tk.Tk()
root.title('PDF upload')
root.geometry("350x350")

button = tk.Button(root, text='Upload a pdf',command=UploadAction)
button.grid(padx=125, pady=150)

root.mainloop()
