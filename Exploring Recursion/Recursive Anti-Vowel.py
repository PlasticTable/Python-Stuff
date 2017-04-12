def anti_vowel(text):
    if text == "":
        return text
    elif text[0] in "AEIOUaeiou":
        return anti_vowel(text[1:])
    else:
        return text[0] + anti_vowel(text[1:])
    
print(anti_vowel("Hey look Words!"))
print(anti_vowel("AAk"))
print(anti_vowel(""))
