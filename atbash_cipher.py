import string

def encode(plaintext):

    # create a translation table that maps each letter to its reverse
    atbash_table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    
    # apply the translation table to the plaintext and remove non-alphabetic characters
    ciphertext = plaintext.lower().translate(atbash_table, string.punctuation + string.whitespace + string.digits)
    
    # group the ciphertext into blocks of 5 letters
    return ' '.join([ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)])
    

def decode(ciphertext):

    # create a translation table that maps each letter to its reverse
    atbash_table = str.maketrans(string.ascii_lowercase[::-1], string.ascii_lowercase)
    
    # apply the translation table to the ciphertext and remove non-alphabetic characters
    plaintext = ciphertext.lower().translate(atbash_table, string.punctuation + string.whitespace + string.digits)
    
    # remove the spaces between blocks of letters and return the plaintext
    return plaintext.replace(' ', '')