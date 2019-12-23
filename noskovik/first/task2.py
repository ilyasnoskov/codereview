"""
Зробити у всіх словах першу букву великою.
"""

text = str(input())
text=text.split()
for elements in text:
    try:
        if elements == elements.isupper:
            print(elements)
    except:
        print()