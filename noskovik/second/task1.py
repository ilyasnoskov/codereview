"""
Знайти мінімальне слово за кількістю букв.
"""

import re


text=input()
def find_text(text):

    a = re.findall('\w*[A-Za-z]', text)
    for element in a:
        min(b) = int(len(element))

        return print(min)

find_text(text)