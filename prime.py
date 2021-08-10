# Accept number from user and check whether it is prime or not
# input : 7
# output : True
# input : 2
# outpu : False
def CheckPrime(no):
    iCnt = 2 
    for i in range(1,int(no/2)):       # no = 7
        if((no % iCnt) == 0):
            break;
        iCnt = iCnt + 1
        
    if (iCnt == int(no/2)+1):
        return True
    else:
        return False
       
    
    #while(iCnt <= no/2):
        #if((no % iCnt) == 0):
            #break;
        #iCnt = iCnt + 1
        
    #if (iCnt == int(no/2)+1):
        #return True 
    #else:
        #return False
    
def main():
    print("Enter the number")
    value = int(input())
    print("*****************************") 
    bret  =  CheckPrime(value)
    if(bret == True):
        print("It is prime number")
    else:
        print("It is not prime number")
    print("*****************************")  

if __name__=="__main__":
    main()