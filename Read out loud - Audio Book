#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3 PyPDF2 


# In[2]:


pip install googletrans


# In[3]:


import pyttsx3
import PyPDF2
from googletrans import Translator


# In[4]:


readbook = open('Story.pdf', 'rb')   
pdfReader = PyPDF2.PdfFileReader(readbook)
pages = pdfReader.numPages

readloud = pyttsx3.init()
for num in range(pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        print(text)
        readloud.say(text)
        readloud.runAndWait()
        

