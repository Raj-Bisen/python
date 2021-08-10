# Accept number from user and return Multiplication of digits .
# input :      1415
# output :      5*1*4*1=  20
def MultiplicationDigits(no):
    iDigit = 0
    iMult = 1
    while (no != 0):
        iDigit = int(no % 10)
        iMult = iMult * iDigit
        no = int(no / 10)
    return iMult
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    ret = MultiplicationDigits(value)
    print("Multiplication of digits is : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()