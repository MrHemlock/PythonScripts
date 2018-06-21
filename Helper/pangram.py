import string
def is_pangram(name):
    a=name.lower()
    for let in string.ascii_lowercase:
        if let not in a:
            return False
    return True


result=is_pangram("The quick brown fox jumps over the lazy dog")
print(result)