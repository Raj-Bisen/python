# Accept number from user and return its Reverse  number .
# input :      1425
# output :      5241
def ReverseNumber(no):
    iDigit = 0
    iRev = 0
    while (no > 0):
        iDigit = int(no % 10)
        iRev = (iRev * 10)+iDigit
        no = int(no / 10)
    return iRev
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    ret = ReverseNumber(value)
    print("After reverse number is  : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()