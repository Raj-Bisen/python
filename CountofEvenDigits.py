# Accept number from user and return count of Even digits from that number .
# input :      2435
# output :     2
def CountEvenDigits(no):
    iDigit = 0
    iCnt = 0
    while (no != 0):
        iDigit = int(no % 10)
        if iDigit % 2 == 0:
            iCnt = iCnt + 1
        no = int(no / 10)
    return iCnt
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    ret = CountEvenDigits(value)
    print("Count  of even digits is : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()