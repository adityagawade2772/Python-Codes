def evenodd(n):

    result = False

    if (n % 2 == 0):
        result = True
    else:
        result = False

    return result   
    #print(result)
    
# evenodd()

def main():
    n = int(input())
    iRet = evenodd(n)
    print(iRet)
main()    

