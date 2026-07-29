
# second maximum number in a list
def main():
    lst = list(map(int, input().split()))
    max = lst[0]
    second_max = None
    for i in lst:
        if i > max:
            max = i
    for i in lst:
        if (second_max is None or i > second_max) and i < max:
            second_max = i

    print(second_max)

main()