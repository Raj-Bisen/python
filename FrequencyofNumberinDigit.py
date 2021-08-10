# Accept number from user and return Frequency of 2nd number .
# input :      2435
# output :     2
def Frequency(no, i):
    iDigit = 0
    iCnt = 0
    while(no != 0):
        iDigit = int(no % 10)
        if(iDigit == i):
            iCnt = iCnt + 1
        no = int(no / 10)
    return iCnt
    
def main():
    print("Enter the number")
    value1 = int(input())
    
    print("Enter the number to find frequency")
    value2 = int(input())
    print("*****************************") 
    ret = Frequency(value1,value2)
    print("Frequency of 2nd number is  : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()