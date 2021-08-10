# Accept number from user and return Largest digit from that number.
# input : 4529
# output : 9

def LargestDigit(no):
    iDigit = 0
    iMax = 0
    while(no > 0):
        iDigit = int(no % 10)
        if iDigit > iMax:
            iMax = iDigit
        no = int(no / 10)
    return iMax
    
def main():
    print("Enter the number")
    value = int(input())
    print("*************************")
    ret = LargestDigit(value)
    print("Largest Digit is :",ret)
    print("*************************")

if __name__=="__main__":
    main()