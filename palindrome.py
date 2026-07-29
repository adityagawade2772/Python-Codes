def simple():
    str = input()
    rev= ""
    for i in str:
        rev = i + rev
    if str == rev:
        print(True)
    else:
        print(False)

def two_pointer():
    str = input()

    left = 0
    right = len(str) -1
    while left< right:
        if str[left] == str[right]:
            left +=1
            right -= 1
        else:
            return False
    return True



# simple()

# a = two_pointer()
# print(a)

def palindrome_hash_freq():
    a = input()
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) +1 

    odd = 0
    for count in freq.values():
        if count % 2 != 0:
            odd += 1

    return odd <= 1

a = palindrome_hash_freq()
print(a)


