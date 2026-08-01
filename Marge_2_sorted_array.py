# marge 2 sorted array without duplicate

def marge_array(num1, num2):
    n = len(num1)
    m = len(num2)
    result = []
    i = 0
    j = 0

    while (i < n and j < m):
        if (num1[i]<num2[j]):
            if(len(result)==0 or result[-1] != num1[i]):
                result.append(num1[i])

            i += 1

        if (num2[j]<num1[i]):
            if (len(result)==0 or result[-1] != num1)