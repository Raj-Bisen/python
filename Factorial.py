# Accept number from user and return its factorial.
#input : 5
#ouput : 120
def Factorial(no1):
    
    iCnt = 1 
    iMult = 1
    #for i in range(no1):       # no1 = 4
        #iMult = iMult * iCnt
        #iCnt = iCnt +1
    #return iMult
    
    while(iCnt <= no1):
        iMult = iMult * iCnt
        iCnt = iCnt + 1
    return iMult
    
  
    
def main():
    print("Enter the number")
    value1 = int(input())
    print("**************************") 
    bret = Factorial(value1)
    print("Factorial  is : ",bret)
    print("**************************") 

if __name__=="__main__":
    main()