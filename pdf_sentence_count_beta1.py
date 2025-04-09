# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:40:35 2025

@author: eanna
"""

import PyPDF2
import nltk
nltk.download('punkt')  # Only needed once to download tokenizer data
from nltk.tokenize import sent_tokenize

def count_sentences_per_page(file_path):
    sentence_counts = {}
    total_sentences = 0
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                sentences = sent_tokenize(text)
                count = len(sentences)
                sentence_counts[f"Page {i+1}"] = count
                total_sentences += count
            else:
                sentence_counts[f"Page {i+1}"] = 0
    return sentence_counts, total_sentences

def print_sentence_counts(sentence_counts, total_sentences):
    for page, count in sentence_counts.items():
        print(f"{page}: {count} sentence{'s' if count != 1 else ''}")
    print("\nTotal sentence count:", total_sentences)

if __name__ == "__main__":
    # Update this path accordingly (using a raw string to handle Windows backslashes)
    file_path = r"C:\Users\eanna\Downloads\stor_editor_882\input\Raiteas_Straiteise_2023-2026_Statement_of_Strategy.pdf"
    counts, total = count_sentences_per_page(file_path)
    print_sentence_counts(counts, total)


