# Accept number from user and return Difference between Summation of its   factors and non factors
# input : 6
# output : 1 + 2 + 3 = 6     ,   4  +  5  =  9
# final output =  6 -  9 = -3
def Difference(no):
    iCnt = 1 
    iSum1 = 0
    iSum2 = 0
    for i in range(1,no):       # no1 = 6
        if((no % iCnt) == 0):
            iSum1 = iSum1 + iCnt
        else:
            iSum2 = iSum2 + iCnt
        iCnt = iCnt + 1
    return iSum1 - iSum2
       
    
    #while(iCnt <= no):
        #if((no % iCnt) == 0):
            #iSum1 = iSum1 + iCnt
        #else:
            #iSum2 = iSum2 + iCnt
        #iCnt = iCnt + 1
    #return iSum2 - iSum1
    
def main():
   
    print("Enter the number")
    value1 = int(input())
    
    print("*****************************") 
    
    ret  =  Difference(value1)
    print("Difference  is : ",ret)
    
    print("*****************************")  

if __name__=="__main__":
    main()