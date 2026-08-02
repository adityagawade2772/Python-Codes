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
            if (len(result)==0 or result[-1] != num1):
                result.append(num2[j])
            j += 1

    while(i < n):
        if(len(result)==0 or result[-1] != num1[i]):
            result.append(num1[i])
        i += 1

    while(j < m):
        if (len(result)==0 or result[-1] != num1):
            result.append(num2[j])
        j += 1

    return(result)
        
def main():
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    a = marge_array(num1 , num2)
    print(a)
main()