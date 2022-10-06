codes = {
    'A': '~',
    'B': '+',
    'C': '`',
    'D': '=',
    'E': '!',
    'F': '5',
    'G': '-',
    'H': '@',
    'I': '_',
    'J': '#',
    'K': ')',
    'L': '$',
    'M': '(',
    'N': '%',
    'O': '*',
    'P': '^',
    'Q': '&',
    'R': '{',
    'S': '?',
    'T': '}',
    'U': '>',
    'V': ':',
    'W': '<',
    'X': '"',
    'Y': '|',
    'Z': '[',
    '0': '/',
    '1': ']',
    '2': '.',
    '3': ';',
    '4': ',',
    '5': "'",
    '6': "1",
    '7': '4',
    '8': '0',
    '9': '7',
    ' ': ' '
}

def encryption(text):
    encrypted_text=''
    for letters in text:
        if letters != " ":
            encrypted_text+=codes.get(letters)
        else:
            encrypted_text+=' '
    print(encrypted_text)

def decryption(text):
    codes_keys=list(codes.keys())
    codes_values=list(codes.values())
    original=''
    for letter in text:
        if text != ' ':
            original+=(codes_keys[codes_values.index(letter)])
    print(f'Your encrypted code is: {original}')
                

text=input("Press 'E' to encrypt or 'D' to decrypt: ").upper()
if text=='E':
    try:
        text_encrypt=input('Enter text to encrypt: ').upper()
        print('\t')
        encryption(text_encrypt)
    except:
        print('You can only enter alphanumeric characters which do not include special symbols!')
    if input('Press any key to exit: ').upper() == 'X':
        exit() 
elif text=='D':
    try:
        text_decrypt=input('Enter code to decrypt: ')
        print('\t')
        decryption(text_decrypt)
    except:
        print('This is not a encrypted code!')
    if input('Press any key to exit: ').upper() == 'X':
        exit() 
else:
    print('Enter valid key!')
    if input('Press any key to exit: ').upper() == 'X':
        exit()

