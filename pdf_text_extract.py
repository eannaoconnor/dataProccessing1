# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 11:28:11 2025

@author: eanna
"""
from pypdf import PdfReader

pdf_reader = PdfReader(r'C:\Users\eanna\Downloads\stor_editor_882\input\Raiteas_Straiteise_2023-2026_Statement_of_Strategy.pdf')
page_content = {}

for indx, pdf_page in enumerate(pdf_reader.pages):
    page_content[indx + 1] = pdf_page.extract_text()
    
print(page_content)