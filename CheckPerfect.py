# Accpet number from user and check whether number is perfect or not.
#input : 6  , 28
# output : True
#input : 4
#output : False

def PerfectNum(no):
    iCnt = 1 
    iSum = 0
    while(iCnt <= no/2):
        if((no % iCnt) == 0):
            iSum = iSum + iCnt
        iCnt = iCnt + 1
    if(iSum == no):
        return True
    else:
        return False
    
    #for i in range(1,int(no/2)+1):
        #if no % i == 0 :
            #iSum = iSum + i
    #if(iSum == no):
        #return True
    #else:
        #return False
        
def main():
    print("Enter the number")
    value1 = int(input())
    print("*****************************") 
    bret  =  PerfectNum(value1)
    if(bret == True):
        print("It is perfect number")
    else:
        print("It is not perfect number")
    print("*****************************")  

if __name__=="__main__":
    main()