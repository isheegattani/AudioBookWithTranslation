#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pyttsx3 pdfplumber PyPDF2


# In[ ]:


pip install googletrans


# In[ ]:


import pyttsx3
import pdfplumber
import PyPDF2
from googletrans import Translator


# In[ ]:


readbook = open('Spain.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(readbook)
pages = pdfReader.numPages

readloud = pyttsx3.init()
for num in range(pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        translator=Translator()
        translation = translator.translate(text, dest="en")
        translated = str(translation.text)
        print(translated)
        readloud.say(translated)
        readloud.runAndWait()
        

