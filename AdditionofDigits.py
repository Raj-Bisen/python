# Accept number from user and return addition of digits .
# input :      1435
# output :      5+3+4+1=  13
def AdditionDigits(no):
    iDigit = 0
    iSum = 0
    while (no != 0):
        iDigit = int(no % 10)
        iSum = iSum + iDigit
        no = int(no / 10)
    return iSum
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    ret = AdditionDigits(value)
    print("Addition of digits is : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()