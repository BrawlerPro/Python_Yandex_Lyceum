def palindrome():
    with open('input.dat', 'rb') as file:
        data = file.read()
        if data == reversed(data):
            return True
        return False
