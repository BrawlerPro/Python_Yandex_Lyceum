big_words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_caesar(msg, shift=1):
    output_text = ''
    for word in msg:
        if word in big_words:
            output_text += big_words[big_words.index(word) + shift - 1]
        elif word in low_words:
            output_text += low_words[low_words.index(word) + shift - 1]
    return output_text


print(encrypt_caesar('Abc', 4))