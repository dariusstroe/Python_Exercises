"""
Stroye language
vocala -> x

dog -> dgx
"""

def Translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"X"
            else:
                translation=translation+"x"
        else:
            translation=translation+letter
    return translation

print(Translate(input("Enter a phrase: ")))

#this is a comment