

def caesarCipher(s, k):
    """ 
    Input: String s, Int k
    Output: encrypted string  
    """
    # Write your code here
    encrypted_message = ''
    if k>=26:
        k = k%26
    for i in s:
        letter = ord(i)
        # only shift letter if it is alphabet

        # capital letters
        if letter>=65 and letter<=90-k:
            shifted = chr(letter+k)
        elif letter>90-k and letter<=90:
            shifted = chr((letter+k)%90 + 64)
        
        # lower case
        elif letter>=97 and letter<=122-k:
            shifted = chr(letter+k)
        elif letter>122-k and letter<=122:
            shifted = chr((letter+k)%122 + 96)

        else:
            shifted = chr(letter)
        encrypted_message += shifted
        # print(i+k)

    return encrypted_message

    



if __name__ == '__main__':
    original_message = "z"
    shift = 27
    print(caesarCipher(original_message, shift))