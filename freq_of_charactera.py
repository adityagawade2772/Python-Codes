def count_freq_character(str):
    freq= {}
    for i in str:
        freq[i] = freq.get(i, 0)+1
    return(freq)


def first_non_repeting_char(str):
    freq= {}
    for i in str:
        freq[i] = freq.get(i, 0) + 1
    for ch in str:
        if freq[ch] == 1:
            print(ch)
            return
    print("No non-repeating character")




def main():
    inp = input("Enter String: ")
    # a = count_freq_character(inp)
    first_non_repeting_char(inp)
main()
