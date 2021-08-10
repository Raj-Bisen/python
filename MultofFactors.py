# Accept number from user and return multiplication of its  factors
# input : 6
# output : 1 * 2 * 3 = 6
def MultFactors(no):
    iCnt = 1 
    iMult = 1
    for i in range(1,int(no/2)+1):       # no = 6
        if  no % iCnt == 0:
            iMult = iMult * iCnt
        iCnt = iCnt +1
    return iMult
    
    #while(iCnt <= no/2):
        #if((no % iCnt) == 0):
            #iMult = iMult * iCnt
        #iCnt = iCnt + 1
    #return iMult
    
def main():
   
    print("Enter the number")
    value = int(input())
    
    print("***********************************") 
    
    ret  =  MultFactors(value)
    print("Multiplication of factors is : ",ret)
    
    print("***********************************")  

if __name__=="__main__":
    main()