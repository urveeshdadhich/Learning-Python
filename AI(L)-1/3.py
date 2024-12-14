#WAP to sort the character of a string and first alphabet symbols followed by numerical value

s = "a1b3dc4"

alphabets = sorted([char for char in s if char.isalpha()])
digits = sorted([char for char in s if char.isdigit()])

result = ''.join(alphabets+digits)
print(result)