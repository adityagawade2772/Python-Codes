def main():
    array = list(map(int, input().split()))

    result = 0
    avg = 0

    for i in array:
        result += i

    avg = result / len(array)
    print(avg)


main()