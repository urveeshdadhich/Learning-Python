#WAP to display all positions of subsrings in a given main string
#main : abbbabbccdeeffaabba
#sub : a

S = "abbbabbccdeeffaabba"
n = len(S)
start = 1  # Start searching from index 1

while start < n:
    pos = S.find('a', start, n)
    if pos == -1:  # No more 'a' found
        break
    print(f"'a' found at index: {pos}")
    start = pos + 1  # Increment start to search for the next 'a'


