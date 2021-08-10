# Accept number from user and return Diffrence between largest and smallest digit.
# input : 4529
# output : 9 - 2 = 7

def Difference(no):
    iDigit = 0
    iMax = 0
    iMin = 9
    while(no > 0):
        iDigit = int(no % 10)
        if iDigit > iMax:
            iMax = iDigit
        elif iDigit < iMin:
            iMin = iDigit
        no = int(no / 10)
    return iMax - iMin
    
def main():
    print("Enter the number")
    value = int(input())
    print("*************************")
    ret = Difference(value)
    print("Difference between Largest & Smallest digit is :",ret)
    print("*************************")

if __name__=="__main__":
    main()