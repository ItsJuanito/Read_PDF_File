import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book) # The file goes in here
pages = pdfreader.numPages # This will return you the number of pages in the pdf

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText() # Extracting all the text from the page
    player = pyttsx3.init()
    player.say(text) # The play will say the text
    player.runAndWait() # This will run the player
# The for loop will iterate through all of the pages in the file