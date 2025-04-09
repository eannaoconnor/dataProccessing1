# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:30:57 2025

@author: eanna
"""

import docx
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def count_sentences_in_docx(docx_path):
    
    doc =docx.Document(docx_path)
    full_text = "\n".join(para.text for para in doc.paragraphs if para.text.strip())
    sentences = sent_tokenize(full_text)
    return len(sentences)

if __name__ ==  "__main__":
    docx_path = r""
    total_sentences = count_sentences_in_docx(docx_path)
    print(f"Total sentences in this document:{total_sentences}")