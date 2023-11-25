#!/usr/bin/env python3

def return_evens(sequence):
    even_numbers = [num for num in sequence if num % 2 == 0]
    return even_numbers

def make_exclamation(sentences):
    exclaimed_sentences = [sentence + '!' for sentence in sentences]
    return exclaimed_sentences