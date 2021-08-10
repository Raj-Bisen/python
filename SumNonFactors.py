# accept number from user and return Summation of its non factors
# input : 6
# output : 4  +  5 = 9
def SumNonFactors(no):
    iCnt = 1
    iSum = 0    
    for i in range(1,no):       # no1 = 6
        if no % iCnt != 0 :
            iSum = iSum + iCnt
        iCnt = iCnt +1
    return iSum
    
    #while(iCnt <= no):
        #if((no % iCnt) != 0):
            #iSum = iSum + iCnt
        #iCnt = iCnt + 1
    #return iSum
    
def main():
    print("Enter the number")
    value = int(input())
    print("**************************") 
    ret = SumNonFactors(value)
    print("Summation of non factors is : ",ret)
    print("**************************") 

if __name__=="__main__":
    main()