#Simple Pin-Extractor from Poems

#How it works in steps:
#1. Splits each poem into lines.
#2. Splits each line into words.
#3. If the word at the current line exists -> add the length of that word to the pin.
#4. Else, it should add '0'.
#5.Repeat for all poems to return the secret code or other words, the pin.


#running the program 

def pin_extractor(poems): 
    """Returns a generic pin code from each poem based on word lengths."""
    secret_codes = []

    for poem in poems:
        secret_code = ''
#Splits the poem into lines
        lines = poem.split('\n')

#Splits the line into words
        for line_index, line in enumerate(lines):
            words = line.split() 

 #Length of word at this index or 0( if not avaliable)
            if len(words) > line_index: 
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    
    return secret_codes

#Examples
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = '''The grass is green 
here and there
hoping for rain
before it turns yellow'''

poem3 = '''There
once
was
a
dragon'''


print(pin_extractor([poem, poem2, poem3]))




