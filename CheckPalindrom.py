# Accept number from user and check whether it is palindrom or not .
# input :      141
# output :    True
# input :       123
# output :     False
def CheckPalindrom(no):
    iDigit = 0  
    iRev = 0
    iTemp = 0
    iTemp = no
    while (no > 0):
        iDigit = int(no % 10)
        iRev = (iRev * 10)+iDigit
        no = int(no / 10)
    if (iRev == iTemp):
        return True
    else:
        return False
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    bret = CheckPalindrom(value)
    if (bret == True):
        print("Number is palindrom")
    else:
        print("number is not palindrom")
    print("*****************************")  

if __name__=="__main__":
    main()