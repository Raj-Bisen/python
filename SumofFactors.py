# Accept number from user and return addition of its  factors
# input : 6
# output : 1 + 2 + 3 = 6
def AdditionFactors(no):
    iCnt = 1 
    iSum = 0
    for i in range(1,int(no/2)+1):       # no1 = 6
        if no % iCnt == 0:
            iSum = iSum + iCnt
        iCnt = iCnt +1
    return iSum
    
    #while(iCnt <= no/2):
        #if((no % iCnt) == 0):
            #iSum = iSum + iCnt
        #iCnt = iCnt + 1
    #return iSum
    
def main():
    print("Enter the number")
    value1 = int(input())
    print("*****************************") 
    ret  =  AdditionFactors(value1)
    print("Addition of factors is : ",ret)
    print("*****************************")  

if __name__=="__main__":
    main()