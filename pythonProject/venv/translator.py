# giraffe translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":       # additionally letter.lower() chooses the lowercase
            translation = translation + "g"
            if letter.isupper():
                translation = translation + "G" # keeps capital if original letter is capital
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a Phrase: ")))

'''
This is how you make comments on multiple lines; 3 single quotes.
'''

