# Accept number from user and return Smallest digit from that number.
# input : 4529
# output : 2

def  SmallestDigit(no):
    iDigit = 0
    iMin =9
    while(no > 0):
        iDigit = int(no % 10)
        if iDigit < iMin:
            iMin = iDigit
        no = int(no / 10)
    return iMin
    
def main():
    print("Enter the number")
    value = int(input())
    print("*************************")
    ret = SmallestDigit(value)
    print("Smallest Digit is :",ret)
    print("*************************")

if __name__=="__main__":
    main()